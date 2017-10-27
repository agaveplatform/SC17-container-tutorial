#!/bin/bash

# if starting on a host without a public ip address, a reverse tunnel must be
# started to make the host availble to the outside world.
if [[ 'True' == "$USE_TUNNEL" ]]; then
  echo "Starting ngrok tunnel..."
  /usr/local/bin/tunnelup.sh

  
fi

exec "$@"
