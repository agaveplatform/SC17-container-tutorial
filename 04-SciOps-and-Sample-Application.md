# Introduction

Now that you have your login and VM set up, we will introduce the concept of containerized SciOps using our example application, [FUNWAVE-TVD](https://github.com/fengyanshi/FUNWAVE-TVD). In the interests of time, we will assume you already have a passing familiarity with version control, one or more container technologies, cloud services, and asynchronous automation. For more information on these topics, please see the [References](99-References.md] section.

# SciOps

SciOps is a software development and digital science methodology that emphasizes reproducibility, collaboration, and technology agnosticism between research, software development, and experimental science. A common sciops lifecycle can be broken down into the following steps.

* Code — code development and review, source code management tools, code merging
* Build — continuous integration tools, build status
* Test — continuous testing tools that provide feedback on business risks
* Package — artifact repository, application pre-deployment staging
* Release — change management, release approvals, release automation
* Experiment - apply the code to a predefined experimental process
* Archive - persist the provenance around the experiment for long-term reference
* Analyze - scrutinize the experimental process and outcome. (This may involve further experimentation.)
* Publish - make results available for collaborative access
* Communicate - share results of experiment, analysis, or raw data with others
* Collaborate - engage others in the experiement or results
* Promote - advertise results for external review and accessability
* Preserve - store results for long-term archiving

![alt text](sciops_big_picture.png "SciOps big picture diagram")

We will reference each of these steps as we progress through the tutorial demonstrating their hands-on application.



# Next Steps
We will apply a SciOps process to our FUNWAVE-TD application to show how we can realize greater portability and reproducibility from our existing processes through the use of some common cloud and container services. The following image shows the big picture diagram of what our overall process will look like once we are done.   



The remainder of this section will cover the following steps in the SciOps process:

1. [Building](notebooks/Build-and-Test.md): compiling & building, version control, build automation
2. [Containerization](notebooks/Containerization-and-Automation.md): image build files, metadata, image portability, and container automation
3. [Publishing](): publishing, promoting, and distributing images
4. [Running](): running containers vs container runtimes, data scheduling and management, monitoring
