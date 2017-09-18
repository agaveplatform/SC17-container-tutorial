> This document is also available as an interactive Jupyter notebook ([05-Code-Build-and-Run-Locally.ipynb](notebooks/05-Code-Build-and-Run-Locally.ipynb)) where you can build, run, and interact with the application code directly.  

# FUNWAVE-TVD

> [FUNWAVE-TVD](https://github.com/fengyanshi/FUNWAVE-TVD) is the TVD version of the fully nonlinear Boussinesq wave model (FUNWAVE) initially developed by Kirby et al. (1998). The development of the present version was motivated by recent needs for modeling of surfzone–scale optical properties in a Boussinesq model framework, and modeling of Tsunami wave in both a regional/coastal scale for prediction of coastal inundation and a basin scale for wave propagation. This version features several theoretical and numerical improvements, including 1) a more complete set of fully nonlinear Boussinesq equations; 2) MUSCL–TVD solver with adaptive Runge–Kutta time stepping; 3) Shock–capturing wave breaking scheme; 4) wetting–drying moving boundary condition with incorporation of HLL construction method into the scheme; 5) an option for parallel computation.

We will be using FUNWAVE as our example code, rather than the usual `/bin/date` or `cowsay` examples because it represents a real-world code with significant dependencies and code complexity as well as the ability to leverage OpenMP to run across multiple nodes. We will start from a the project source code, build an run the code locally on our workshop VM, then walk you through the process of containerizing, automating, and publishing the code in a portable manner.

## Requirements
> **TODO:** @stevenrbrandt Would you please fill in the usual blurb here  

Your sandbox has been preconfigured with all the requirements needed to build and run FUNWAVE-TVD. If you are following along in the jupyter hub, you can skip straight to the installation step.

## Installation
> **TODO:** @stevenrbrandt Would you please fill in the usual blurb here

```
cd ~/FUNWAVE_TVD/src
perl -p -i -e 's/FLAG_8 = -DCOUPLING/#$&/' Makefile
make
```  

## Running
> **TODO:** @stevenrbrandt Would you please fill in the usual blurb here
```
cd ~/FUNWAVE_TVD/src
./funwave_vessel
```

1. [Building](notebooks/Build-and-Test.md): compiling & building, version control, build automation
2. [Containerization](notebooks/Containerization-and-Automation.md): image build files, metadata, image portability, and container automation
3. [Publishing](): publishing, promoting, and distributing images
4. [Running](): running containers vs container runtimes, data scheduling and management, monitoring
