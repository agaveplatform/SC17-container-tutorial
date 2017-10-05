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
COPY motd /etc/update-motd.d/00-header
RUN chmod 755 /etc/update-motd.d/00-header


#RUN dnf -y install gcc-c++ gcc-gfortran which findutils python3 python3-pip wget make git patch flex && \
#WORKDIR /home
#RUN wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.gz
#RUN tar xzvf openmpi-2.1.1.tar.gz
#WORKDIR /home/openmpi-2.1.1
#RUN ./configure
#RUN make -j 5 install
#
#RUN adduser funw
#USER funw
#
##ENV LD_LIBRARY_PATH="/usr/lib64/openmpi/lib"
##ENV MPI_FORTRAN_MOD_DIR="/usr/lib64/gfortran/modules/openmpi";
##ENV PATH="/usr/lib64/openmpi/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/funw/.local/bin:/home/funw/bin";
##ENV PKG_CONFIG_PATH="/usr/lib64/openmpi/lib/pkgconfig";
#WORKDIR /home/funw
#
#RUN git clone https://github.com/fengyanshi/FUNWAVE-TVD
#
#WORKDIR /home/funw/FUNWAVE-TVD/src
#RUN perl -p -i -e 's/FLAG_8 = -DCOUPLING/#$&/' Makefile
#RUN make
#RUN chmod 755 /home/funw
