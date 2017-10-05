FROM ubuntu:16.04

MAINTAINER Rion Dooley <deardooley@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV TEST_USERNAME jovyan

RUN apt-get update -qqq && \
    apt-get install -y apt-utils debconf-utils wget curl openssl ssh

    # install Docker -- this will put the cli binary in the image. you will still
    # need to bind mount the docker socket into the host for it to work...
RUN    apt-get install -y apt-transport-https ca-certificates software-properties-common && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial edge" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce

    # Singularity binary distro is shipped from the neurodebian mirror
RUN    wget -O- http://neuro.debian.net/lists/xenial.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list && \
    apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9 && \
    apt-get update -qqq && \
    apt-get install -y  --allow-unauthenticated singularity-container && \

    # cleanup after yourself
    apt-get clean


RUN adduser "$TEST_USERNAME" && \
    echo "$TEST_USERNAME:$TEST_USERNAME" | chpasswd

RUN mkdir -p /var/run/sshd && \
    sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config; \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd; \
    sed -i 's/^exit 0/service ssh start\nexit 0/' /etc/rc.local && \
    /usr/bin/ssh-keygen -A

ADD ssh/id_rsa.pub /home/$TEST_USERNAME/.ssh/authorized_keys
ADD ssh/id_rsa.pub /home/$TEST_USERNAME/.ssh/id_rsa.pub
ADD ssh/id_rsa /home/$TEST_USERNAME/.ssh/id_rsa

RUN chmod 700 /home/$TEST_USERNAME/.ssh && \
    chmod 600 /home/$TEST_USERNAME/.ssh/authorized_keys && \
    chown -R $TEST_USERNAME /home/$TEST_USERNAME/.ssh && \
    usermod -a -G docker "$TEST_USERNAME"

RUN apt-get install -y python-pip && \
    pip install supervisor

ADD supervisord.conf /etc/supervisord.conf
ARG BUILD_DATE
ARG VERSION

LABEL org.agaveplatform.devops.architecture="x86_64"                                 \
      org.agaveplatform.devops.build-date="$BUILD_DATE"                              \
      org.agaveplatform.devops.license="BSD 3-clause"                                \
      org.agaveplatform.devops.name="agaveplatform/ssh-sanbox"                       \
      org.agaveplatform.devops.summary="SSH login node to provide user sanboxes for trainings" \
      org.agaveplatform.devops.version="$VERSION"                                    \
      org.agaveplatform.devops.vcs-type="git"                                        \
      org.agaveplatform.devops.vcs-url="https://github.com/agaveplatform/ssh-sanbox" \
      org.agaveplatform.devops.jupyter.version="5.0.x"                               \
      org.agaveplatform.devops.environment="training"                                \
      org.agaveplatform.training="jupyter"

EXPOSE 22
CMD ["/usr/local/bin/supervisord"]
