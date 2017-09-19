> This document is also available as an interactive Jupyter notebook ([06-Containerize-Existing-Applications.ipynb](content/notebooks/06-Containerize-Existing-Applications.ipynb)) where you can build, run, and interact with the application containers directly.  

# Container technology
Container technologies have exploded over the last 5 years. In the scientific computing space, [Docker](https://docker.com) dominates overall utilization and adoption. Within the HPC space, where concerns over security, performance, and legacy integration are primary, [Singularity](http://singularity.lbl.gov/) has arisen to fill the need Docker did not satisfy. While there are certainly other container technologies in use today, we will focus our attention on leveraging the synergy between Docker and Singularity in realizing a SciOps environment for this tutorial.

We assume that the user has a passing familiarity with at least one of these two technologies. Where appropriate, we will provide specific commentary on a specific technology with respect to the task at hand. Deep discussion of the features, strengths, and weaknesses of each technology is beyond the scope of this tutorial. We refer you to the [References section](99-References.md#Container-technologies) for further reading.

> This is by no means a complete list. Shifter, LXC, and OpenVZ are also commonly used in HPC environments, however given the length of this tutorial, the audience at SC, and the rate of adoption seen by Singularity at the time of this tutorial, we limit our scope in this tutorial to Docker and Singularity. Please see the [References section](99-References.md#Container-technologies) for links to articles, projects, and futher reading on these and other container technologies.  


# Portability in practice
Both Docker and Singularity, for the most part, live up to their claim of build once, run anywhere portability. Two specific exceptions to this are worth noting.

## Runtime not included

## Kernels, hardware, and proprietary software

# SciOps considerations

* attribution
* transparency
* documentation
* publication
* usability
* conventions
* benchmarks

# Base image basics

## Base images vs dependency management

## When to trust (and when not to)

## Leveraging community efforts

# Containerizing an example app


## Docker build

Here is the Dockerfile used to build FUNWAVE-TVD  

```
FROM ubuntu:16.04

MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>

# add build tools and python to the sandbox
RUN apt-get install -y --allow-unauthenticated build-essential findutils python3 python3-pip wget make git patch flex gfortran && \
    cd /home && \
    wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.gz && \
    tar xzvf openmpi-2.1.1.tar.gz

# add openmpi 2.1.1
RUN cd /home/openmpi-2.1.1 && \
    ./configure

RUN cd /home/openmpi-2.1.1 && \
    make -j 5 install

ENV LD_LIBRARY_PATH /usr/local/lib

# add application code, funwave-tvd
RUN cd && \
    git clone https://github.com/fengyanshi/FUNWAVE-TVD && \
    perl -p -i -e 's/FLAG_8 = -DCOUPLING/#$&/' Makefile && \
    make

WORKDIR $HOME/FUNWAVE-TVD/src

```

To build the image, we invoke the `docker build` command, providing a name and tag for the image. In the next section, we will discuss the choice of tags an their role in the provenance chain, but for now, we will leave the tag blank and inherit the default, *"latest"* tag.  

```
docker build -rm -t funwave-tvd $(pwd)
```  



## Singularity build

Here is the Singularity build file used to build FUNWAVE-TVD  

```
Bootstrap: docker
From: ubuntu:16.04

%labels
  MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>

%setup
  LD_LIBRARY_PATH /usr/local/lib

%post
  # add build tools and python to the sandbox
  apt-get install -y --allow-unauthenticated build-essential findutils python3 python3-pip wget make git patch flex gfortran
  cd /home
  wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.gz
  tar xzvf openmpi-2.1.1.tar.gz

  # add openmpi 2.1.1
  cd /home/openmpi-2.1.1
  ./configure
  make -j 5 install

  # add demo code, funwave-tvd
  cd $HOME
  git clone https://github.com/fengyanshi/FUNWAVE-TVD

  # build source
  cd FUNWAVE-TVD/src
  perl -p -i -e 's/FLAG_8 = -DCOUPLING/#$&/' Makefile
  make

%runscript
  $HOME/FUNWAVE-TVD/src/funwave_vessel
```

To build the image, we invoke the `singularity bootstrap` command, providing a file name for the image. In the next section, we will discuss the choice of names and labels and their role in the provenance chain, but for now, we will leave the tag blank and inherit the default, *"latest"* tag.  

```
singularity bootstrap ~/funwave.img Singularity
```  

* Container runtimes
* Portability & attribution
* Base images & dependency management
* Multi-stage builds
