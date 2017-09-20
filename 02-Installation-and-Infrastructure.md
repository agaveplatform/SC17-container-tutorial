# Infrastructure

During this tutorial you will primarily interact with two interfaces which will orchestrate multiple cloud services to provide the of the low-level details required to accomplish our goals for today. <span style='color: red'>What are the "two interfaces?"</span> We will be running all the services and development machines used in today's tutorial on the Jetstream cloud.

> If you would like to deploy the tutorial infrastructure yourself on your own machine, please consult the [Appendix A](90-Appendix-A.md) for more details.  

# Architecture
The examples in this tutorial assume the following architecture.

* Training system (dedicated)
* Build system (shared)

## Training system  
Each user has their own "Training system," which will be created shortly after you create your Agave account. Behind the scenes, a training system is just a dedicated Virtual Machine (VM) provisioned on the Jetstream cloud. On that VM are two Docker containers providing the sandbox and notebook environments the user will interact with throughout the tutorial. Both the notebook and the sandbox container share a common file system mounted at the user's home directory.

The Jupyter server is available from their browser at:  

```  
https://<agave-username>-jupyter.training.public.agaveplatform.org.  
```  

*Note: Please avoid using the Safari browser.*

The sandbox is accessible via *ssh* and *sftp*. Users may login to their sandbox using any of the following methods:

```
# Publicly available. Authenticate with the user's Agave Platform password
ssh training@<agave-username>-sandbox.training.public.agaveplatform.org

# Publicly available. Each user's private key is in the home directory of their
# Jupyter server.
ssh -i /path/to/private/key.pem training@<agave-username>-sandbox.training.public.agaveplatform.org

# From the jupyter web terminal. Passwordless ssh has already been configured
# and is available out of the box.
ssh training@<agave-username>-sandbox.training.public.agaveplatform.org

# From the jupyter web terminal. Passwordless ssh has already been configured.
# The sandbox container is visible via the internal hostname `sandbox`
ssh sandbox  
```  

## Build system  
The "build system" hosts a continuous integration server providing automated
builds of your code and doubles as a private registry host for both Docker and
Singularity images.

<span style='color:red'>Do the users interact with this system in any way? Or is it behind-the-scenes magic?</span>

# Cloud Services and Platforms

These are technologies which you will make direct use of during the tutorial.

## Jupyter

The Jupyter is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more.

[Website](http://jupyter.org/) [Project repository](https://github.com/jupyter)

We will be using a Jupyter Notebook as the primary web interface for this workshop. Several notebooks have been provided to you, in advance, to guide you through the workshop. After the workshop, you may use our public Docker image to recreate the notebook server and repeat the workshop, or continue on with your own work at your leisure.   


## The Agave Platform

Agave is an open source, science-as-a-service solution for hybrid cloud computing. It provides a full suite of services covering everything from standards-based authentication and authorization to computational, data, and collaborative services.

[Website](https://agaveplatform.org/) [Project repository](https://github.com/agaveplatform/)

We will be using the Agave Platform to handle much of the orchestration, persistence, and lifecycle management around our application code, sample datasets, and computational runs. Our primary interface to Agave will be through the CLI and Python SDK pre-installed in your Jupyter notebooks.


## JetStream  

Jetstream, led by the Indiana University Pervasive Technology Institute (PTI), adds cloud-based, on-demand computing and data analysis resources to the national cyberinfrastructure. With a focus on ease of use and broad accessibility, Jetstream is designed for those who have not previously used high performance computing and software resources. The system is particularly geared toward 21st-century workforce development at small colleges and universities – especially historically black colleges and universities, minority serving institutions, tribal colleges, and higher education institutions in EPSCoR States.

[Website](https://jetstream-cloud.org/) [Project repository](https://github.com/jetstream-cloud/)
