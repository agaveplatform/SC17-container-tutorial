FROM agaveplatform/ssh-sandbox

MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>

USER root

# add build tools and python to the sandbox
RUN apt-get install -y --allow-unauthenticated build-essential findutils python3 python3-pip wget make git patch flex && \
    cd /home && \
    wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.gz && \
    tar xzvf openmpi-2.1.1.tar.gz

# add openmpi 2.1.1
RUN cd /home/openmpi-2.1.1 && \
    ./configure

RUN cd /home/openmpi-2.1.1 && \
    make -j 5 install

# add demo code, funwave-tvd
RUN cd /home/$TEST_USERNAME && \
    git clone https://github.com/fengyanshi/FUNWAVE-TVD && \
    chown -R $TEST_USERNAME FUNWAVE-TVD

RUN cd /home/$TEST_USERNAME/FUNWAVE-TVD/src && \
    su $TEST_USERNAME -c "perl -p -i -e 's/FLAG_8 = -DCOUPLING/#$&/' Makefile" && \
    su $TEST_USERNAME -c "make" && \
    chmod 755 /home/$TEST_USERNAME && \
    rm -rf /home/openmpi-2.1.1*

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