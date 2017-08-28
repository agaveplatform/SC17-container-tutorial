FROM ubuntu:16.04

MAINTAINER Rion Dooley <deardooley@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qqq && \
    apt-get install -y apt-utils debconf-utils wget curl openssl ssh

RUN wget -O- http://neuro.debian.net/lists/xenial.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list && \
#    apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9 && \
    apt-get update -qqq
RUN apt-get install -y  --allow-unauthenticated singularity-container && \
    apt-get clean


RUN adduser "ubuntu" && \
    echo "ubuntu:ubuntu" | chpasswd

RUN mkdir -p /var/run/sshd && \
    sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config; \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd; \
#    sed -ri 's/UsePAM no/#UsePAM yes/g' /etc/ssh/sshd_config  && \
#    sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  && \
    sed -i 's/^exit 0/service ssh start\nexit 0/' /etc/rc.local && \
    /usr/bin/ssh-keygen -A

ADD ssh/id_rsa.pub /home/ubuntu/.ssh/authorized_keys

RUN chmod 700 /home/ubuntu/.ssh && \
    chmod 600 /home/ubuntu/.ssh/authorized_keys && \
    chown -R ubuntu /home/ubuntu/.ssh


EXPOSE 22
CMD /etc/rc.local; bash