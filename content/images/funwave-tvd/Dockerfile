FROM agaveplatform/ssh-sandbox

MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>

ENV TEST_USERNAME jovyan

USER root

# add build tools and python to the sandbox
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated build-essential findutils python3 python3-pip wget make git patch flex gfortran && \
    apt-get clean

WORKDIR /home
RUN  wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.gz && \
    tar xzvf openmpi-2.1.1.tar.gz && \
    cd /home/openmpi-2.1.1 && \
    ./configure &&  \
    make -j 5 install && \
    cd /home && \
    rm -fr openmpi-2.1.1

USER $TEST_USERNAME

# add demo code, funwave-tvd
RUN cd /home/$TEST_USERNAME && \
    git clone https://github.com/fengyanshi/FUNWAVE-TVD

ENV LD_LIBRARY_PATH /usr/local/lib

WORKDIR /home/$TEST_USERNAME/FUNWAVE-TVD/src

RUN perl -p -i -e 's/FLAG_8 = -DCOUPLING/#$&/' Makefile
RUN make
RUN chown $TEST_USERNAME:$TEST_USERNAME /home/$TEST_USERNAME
RUN echo "\nexport LD_LIBRARY_PATH=/usr/local/lib\n" >> /home/$TEST_USERNAME/.profile
USER root
RUN mv /etc/update-motd.d/00-header /etc/update-motd.d/10-help-text && \
    sed -i 's/^AcceptEnv.*//' /etc/ssh/sshd_config
COPY etc/motd /etc/update-motd.d/00-header
RUN chmod 755 /etc/update-motd.d/00-header

RUN find /home/$TEST_USERNAME | xargs chown $TEST_USERNAME && \
    apt-get install -y vim-tiny nano && \
    echo "includedir /etc/sudoers.d" >> /etc/sudoers && \
    echo "$TEST_USERNAME ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/$TEST_USERNAME && \
    chmod 440 /etc/sudoers.d/$TEST_USERNAME

RUN apt-get install -y unzip jq && \
    curl -sk -o /usr/local/ngrok.zip 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip' && \
    unzip /usr/local/ngrok.zip -d /usr/bin && \
    rm -f /usr/local/ngrok.zip && \
    mkdir /home/$TEST_USERNAME/.ngrok2 && \
    echo "web_addr: 0.0.0.0:4040" >> /home/$TEST_USERNAME/.ngrok2/ngrok.yml && \
    chmod -R 755 /home/$TEST_USERNAME/.ngrok2

RUN echo alias ngrok_url=\""curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' \"" >> /home/$TEST_USERNAME/.bashrc && \
    echo alias ngrok_port=\""curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' |  sed 's|^tcp://||' | sed -r 's#(.*):(.*)#\2#' " \" >> /home/$TEST_USERNAME/.bashrc && \
    echo alias ngrok_host=\""curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' |  sed 's|^tcp://||' | sed -r 's#(.*):(.*)#\1#' " \" >> /home/$TEST_USERNAME/.bashrc && \
    chown -R $TEST_USERNAME /home/$TEST_USERNAME/.ngrok2

# copies ngrok startup scripts to default path
COPY bin/ /usr/local/bin/
COPY etc/supervisord.conf /etc/supervisord.conf
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# RUN mkdir -p /var/log/supervisor && \
#     touch /var/log/supervisor/ngrok.log && \
#     touch /var/log/supervisor/sshd.log

EXPOSE 22 4040

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

CMD ["/usr/local/bin/supervisord"]
