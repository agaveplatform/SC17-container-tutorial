> This document is also available as an interactive Jupyter notebook ([06-Containerize-Existing-Applications.ipynb](content/notebooks/06-Containerize-Existing-Applications.ipynb)) where you can build, run, and interact with the application containers directly.  

# Container technology
Container technologies have exploded over the last 5 years. In the scientific computing space, [Docker](https://docker.com) dominates overall utilization and adoption. Within the HPC space, where concerns over security, performance, and legacy integration are primary, [Singularity](http://singularity.lbl.gov/) has arisen to fill the need Docker did not satisfy. While there are certainly other container technologies in use today, we will focus our attention on leveraging the synergy between Docker and Singularity in realizing a SciOps environment for this tutorial.

We assume that the user has a passing familiarity with at least one of these two technologies. Where appropriate, we will provide specific commentary on a specific technology with respect to the task at hand. Deep discussion of the features, strengths, and weaknesses of each technology is beyond the scope of this tutorial. We refer you to the [References section](99-References.md#Container-technologies) for further reading.

> This is by no means a complete list. Shifter, LXC, and OpenVZ are also commonly used in HPC environments, however given the length of this tutorial, the audience at SC, and the rate of adoption seen by Singularity at the time of this tutorial, we limit our scope in this tutorial to Docker and Singularity. Please see the [References section](99-References.md#Container-technologies) for links to articles, projects, and further reading on these and other container technologies.  


# Portability in practice
Both Docker and Singularity, for the most part, live up to their claim of build once, run anywhere portability. Four specific exceptions to this are worth noting.

## Runtime not included
Regardless of the container technology, the container images created from a `docker build` or `singularity bootstap` operation are ***not*** self-contained executables. They require their respective container engines to setup and start the container process(es). Thus, unless the Docker or Singularity engines are installed on your desired execution system, you will not be able to run a container.

It is worth mentioning that the contrary is not necessarily true. Docker is currently the 800lb gorilla in the container space and, as such, does not support runtimes other than their own Docker Engine**. Competing container technologies such as Singularity, Rocket, and OpenVZ do have the ability to run Docker images either directly or indirectly after a  preprocessing step, or directly.

> ** Technically Docker follows the [Open Container Initiative Runtime Specification](https://github.com/opencontainers/runtime-spec). founded and assures comthey support the RunC spec in their upstream distribution, but that is largely a community driven implementation of their own engine)

## Binary compatibility
The usual caveats around binary portability across kernels also holds with containers. If the host OS cannot support the container kernel, the container cannot run. Thus, a FreeBSD image will not run on a POWER system, and a CentOS7 image will likely not run on a CentOS 5 host. Depending on the container technology, there may be exceptions to this rule. The notable exception being Docker for Windows 10 Pro and higher which starts up a minimal Hyper-V Linux VM capable of running linux containers. Aside from these edge cases, it is safe to say that container portability is generally reliable across Linux systems.

## Hardware dependencies
It is not uncommon for HPC systems to have unique compilers, drivers, and workarounds installed to squeeze as much performance as possible out of their hardware. This generally is not a problem for containers built and run on those systems. It can cause problems when attempting to run the containers on hosts missing the particular hardware or software present on the build system. You might have seen a similar situation occur if you have ever upgraded a video card, or tried to install a new app on a phone more than a few years old.

## Licensing requirements
All licensing and legal concerns are implicitly built into a container. If a license server is required to run a container on one host, the lack of that license server on another host will prevent the container from running. While this is not a technical issue, it still impacts the portability of a container and, therefor, is worth mentioning.


# SciOps considerations

## Attribution
Every container technology supports a mechanism for adding metadata into an image. Including information about the author(s), projects, funding sources, contact information, etc. allows you to receive proper credit for your work.

Leveraging platform infrastructure and using common base images such as BioContainers, Science Apps, and AlogRun, which have informations publishing services bundled into the images, allow usage information as well as attribution information to be collected and made available to authors over time.

## Transparency
Transparency in an image allows trust to build between the author and those using the image. Transparency is also critical for a community to select and rally around a canonical application image. Publishing build instructions, properly tagging and versioning the image, and bundling documentation all allow people on the outside looking in to feel comfortable with incorporating the image into their own work.  

## Documentation  
Without documentation, an image is little more than a black box. Documentation makes the difference between a potential user considering use of your image or scrolling on to the next page in the catalog. Documentation should come in at least two forms. First, the image repository should include a README describing what the image contains, how to use the image, how to build the image, links to the source code repository, license, and maintainer contact info. Second, the image should contain a man or help page that can be invoked by default to show the user how to run the code. A popular convention is to make the application executable run by default, so a new user can always find out how to properly invoke an app by simply starting the container with a `-h` command.

## Publication
People need to be able to find your image if they are going to run your container, so while including a Dockerfile or Singularity build file in your code repository is a great first step, to get broader adoption, consider publishing your image to one of the public registries where others can search and browse for it. Of course, when you do this, think through how, if at all, you will version, document, and support the published image over time.

## Usability  
Containerizing your application gives you the opportunity to control, and often times, improve the user and developer experience associated with your application code. Wrapping your app invocation in a script that handles input validation, file format conversions, sets default values, output transformation, etc. can go a long way to make your application more approachable and open it up to a new audience.

Complex application bundles like [Trinity](https://github.com/trinityrnaseq/trinityrnaseq/wiki), containerized pipelines like [BIDS](http://bids-apps.neuroimaging.io/about/) are sufficiently complicated that it is rare that any one person would leverage all aspects of the application. It is worth considering whether potential users could benefit from the existence of several versions of the image, each preconfigured for a specific use of the tool.

## Conventions  
Along the lines of the usability topic, it is worth considering what conventions can be used to make your application image more approachable. It may be that your potential user community is already so familiar with the application that the best conventions are to simply expose the application exactly as it is. However, it is possible that some of the concepts utilize by your app do not carry over cleanly to a container environment. Inputs, for example, may be better served by allowing users to specify them as arguments rather than inferring a hard coded file name or looking in a specific directory within the container.

Language conventions are another area where you may look for opportunities to adopt conventions. Every language has its own argument parsing library, and every library has slightly different ways of handling arguments, flags, parameters, and ordering. Given that your application is essentially language agnostic when run as a container, you have an opportunity to wrap your application with command line syntax with which your target audience and optimally identify.

## Benchmarks
Generally speaking, there is not much of a performance hit when using containers vs running natively. Most analysis show 1-2% overhead when networking is not involved. However, that does not set expectations about what kind of performance to expect when running your image. Your users may be used to a version compiled with other flags, optimized for other uses, with different defaults set, or without particular modules loaded. The result could be a significant disparity between their experience running your image and the native installation they are used to.

Adding benchmark data to your image, when possible, so others can do an apples to apples comparison of your image vs one they are familiar with can help them understand the implications of using your image. Of course, including your image build file and a README detailing any significant build configuration options is also a good idea. Whenever possible, err on the side of transparency and clarity about what and how your image should be used.

# Base image basics
Chances are that if you are building software of any meaningful complexity, you are leveraging one or more dependency management systems for your language of choice. A full discussion about application portability, software engineering, and software sustainability over time are beyond the scope of this talk. We bring them up here to highlight the many lessons learned from those fields of study over the years and point out that many of the solutions to those problems are difficult to address directly within your application. Things like dependency validation, dependency conflict resolution, security traces, long-tem asset hosting, project sunsets, and technology changes over time can all impact to simply build your application over time, let alone maintain it.

## Base images > dependency management
Base images allow you to standardize and snapshot the common dependencies, processes, configurations, and environments required to build your application. More than simply providing a standard operating system or toolchain, base images can be:

* Places where you standardize your third-party dependencies, alleviating the requirement to call out to a third-party service.
* Checkpoints to automate code quality and consistency.
* [**TODO**] etc, etc, etc

## When to trust (and when not to)


## Leveraging community efforts
Fortunately, a healthy amount of work has gone into defining and field testing base images in many different domains. From BioContainers to Docker's Trusted Registry to CERN's Scientific Linux to Jupyter's Data Science images, a wealth of options are out there to help you get off on the right foot. Even if your situation is such that you cannot adopt them in whole, there is a wealth of information to learn from the authors on what goes into a good base image.

> Further discussion on the challenges of long-term software sustainability, maintenance, and accessibility can be found in the [References section](99-References.md#Scientific-Software-Engineering).

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
