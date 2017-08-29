# Tutorial Setup

## Overview

One of the goals of this tutorial is to teach you how to leverage efforts of dozens of differnet open source projects 
who have invested decades of man-years into the advancement of science, computation, data management, identity and 
access management, security, reproducibility, ui/ux, collaboration, and publishing. While this tutorial is not focused 
on any one specific area, we hope that by providing a consistent, holistic approach to utilizing containers and cloud 
services in your computational and data science research, we can help you accelerate your research velocity and 
improve the reproducibility of your experiments. 

During this tutorial you will primarily interact with two interfaces which will leverage many of the low-level details required to accomplish our goals for today.

### Jupyter 

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more.

[Website](http://jupyter.org/) [Github](https://github.org/jupyter)

We will be using a Jupyter Notebook as the primary web interface for this workshop. Several notebooks have been provided to you, in advance, to guide you through the workshop. After the workshop, you may use our public Docker image to recreate the notebook server and repeat the workshop, or continue on with your own work at your leisure.   


### JetStream  

Jetstream, led by the Indiana University Pervasive Technology Institute (PTI), adds cloud-based, on-demand computing and data analysis resources to the national cyberinfrastructure. With a focus on ease of use and broad accessibility, Jetstream is designed for those who have not previously used high performance computing and software resources. The system is particularly geared toward 21st-century workforce development at small colleges and universities – especially historically black colleges and universities, minority serving institutions, tribal colleges, and higher education institutions in EPSCoR States.

[Website](https://jetstream-cloud.org/) [Github](https://github.com/jetstream-cloud/)


### Agave  

Agave is an open source, science-as-a-service solution for hybrid cloud computing. It provides a full suite of services covering everything from standards-based authentication and authorization to computational, data, and collaborative services.

[Website](https://agaveplatform.org/) [Github](https://github.com/agaveplatform/)

We will be using the Agave Platform to handle much of the orchestration, persistence, and lifecycle management around our application code, sample datasets, and computational runs. Our primary interface to Agave will be through the CLI and Python SDK pre-installed in your Jupyter notebooks. 
 
## Accounts  

We have already created a VM for each of you to use in this workshop. Your VM will serve as a build, compute, and storage system in as we work through the material. Someone will walk around shortly to assign you to a VM. 

### Agave login
While you are waiting for your VM, please create an account on the Agave Platform by filling out the signup form at [https://public.agaveplatform.org](). Please note that you will need to click on the link in your confirmation email to activate your account.  

### Github
You will also need a Github account to leverage the automation we will discuss in the second half of the tutorial. If you do not already have one, please [create a Github account](https://github.com/join).


Once you have confirmed your Agave and Github accounts, please visit the URL assigned to your VM. In the next section we will take a brief tour of the Agave CLI before putting it to use in our SciOps example.

