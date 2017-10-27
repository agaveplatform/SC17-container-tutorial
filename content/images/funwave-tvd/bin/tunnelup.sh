#!/usr/bin/env bash

VERBOSE=1

# get pwd of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

####################################################
# Look for ngrok token to config client for tcp
# connections
####################################################

if [[ -n "$NGROK_TOKEN" ]]; then
  ((VERBOSE)) && printf "Loading ngrok client token..."
  /usr/bin/ngrok authtoken "$NGROK_TOKEN" -log /var/log/ngrok.log 2>&1
else
  ((VERBOSE)) && printf "No NGROK_TOKEN value found in  environment. Skipping client authorization..."
fi


####################################################
# Start a ngrok client so external services can
# access the webhook server from a public URL
####################################################

((VERBOSE)) && printf "Starting a ngrok client..."
/usr/bin/ngrok tcp 22 -log /var/log/ngrok.log 2>&1 &

i=30
while : ; do
    sleep 1
    ((VERBOSE)) && printf "."
    ((i=i-1))
    tunnel=$(curl -s http://localhost:4040/api/tunnels | jq -r ".tunnels[0].public_url")
    [[ "$tunnel" = 'null' ]] && (( $i )) || break
done
((VERBOSE)) && echo "done"

# alias ngrok_port="curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' |  sed 's|^tcp://||' | sed -r 's#(.*):(.*)#\2#' "
# alias ngrok_host="curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' |  sed 's|^tcp://||' | sed -r 's#(.*):(.*)#\1#' "

export VM_HOSTNAME=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' |  sed 's|^tcp://||' | sed -r 's#(.*):(.*)#\1#' )
export VM_IPADDRESS=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' |  sed 's|^tcp://||' | sed -r 's#(.*):(.*)#\1#' )
export VM_SSH_PORT=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' |  sed 's|^tcp://||' | sed -r 's#(.*):(.*)#\2#' )

echo "#############################################################"
echo "# A tunnel has been created for this container to the outside"
echo "# world at: "
echo "#"
echo "#   $VM_HOSTNAME:$VM_SSH_PORT "
echo "#"
echo "# You may ssh into this container using the tunnel address: "
echo "#"
echo "#   ssh -p $VM_SSH_PORT jovyan@$VM_HOSTNAME "
echo "#"
echo "#############################################################"
