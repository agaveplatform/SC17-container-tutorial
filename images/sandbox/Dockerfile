FROM ubuntu:16.04

MAINTAINER Rion Dooley <deardooley@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV TEST_USERNAME jovyan

RUN apt-get update -qqq && \
    apt-get install -y apt-utils debconf-utils wget curl openssl ssh && \

    # Singularity binary distro is shipped from the neurodebian mirror
    wget -O- http://neuro.debian.net/lists/xenial.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list && \
    apt-get update -qqq && \
    apt-get install -y  --allow-unauthenticated singularity-container && \
    apt-get clean


RUN adduser "$TEST_USERNAME" && \
    echo "$TEST_USERNAME:$TEST_USERNAME" | chpasswd

RUN mkdir -p /var/run/sshd && \
    sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config; \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd; \
#    sed -ri 's/UsePAM no/#UsePAM yes/g' /etc/ssh/sshd_config  && \
#    sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  && \
    sed -i 's/^exit 0/service ssh start\nexit 0/' /etc/rc.local && \
    /usr/bin/ssh-keygen -A

ADD ssh/id_rsa.pub /home/$TEST_USERNAME/.ssh/authorized_keys

RUN chmod 700 /home/$TEST_USERNAME/.ssh && \
    chmod 600 /home/$TEST_USERNAME/.ssh/authorized_keys && \
    chown -R $TEST_USERNAME /home/$TEST_USERNAME/.ssh

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
CMD /etc/rc.local; bash