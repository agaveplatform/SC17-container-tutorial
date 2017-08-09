# HPC via HTTP: Portable, Scalable Computing using App Containers and the Agave API

Supercomputing matters. So does user experience. Standing between the mainstream adoption of supercomputing and a new generation of users is the reality that the entry cost to using these systems, both in terms of dollars and in time spent learning the technology, has not significantly changed in the last 20 years. The rise of cloud computing only complicates the learning curve further. Over the last 6 years, the authors have been addressing this gap through the development of a Science-as-a-Service platform enabling users to go from their desktop, to their local data center, to the cloud, and back without sacrificing their existing tool chain or user experience. 

In this tutorial, we combine best practices and lessons learned while on-boarding the last 70k new users to TACC’s data center through the Agave Platform. Participants will walk through the process of scaling their application from a local environment to the Jetstream academic cloud and to a high performance computing system at the Texas Advanced Computing Center. They will learn to use multiple container technologies to harmonize app execution between cloud and HPC resources, and they will learn to use modern APIs to orchestrate job execution, capture provenance information, and foster collaboration.


## Schedule

A. Session I  

|Time           | Topic                                                       |
|---------------|-------------------------------------------------------------|
|  9:30 - 10:00 | [Overview and introductions](overview/readme.md): Introduce instructors and learners. Lay out learning objectives for the morning session. Present an overview of containers and Science-as-a-Service APIs (Presentation and Discussion; 30 minutes)|
|  10:00 - 10:20 | [Connect laptops to on-line resources](setup/readme.md) (hands-on)|
|  10:20 - 12:00 | [Software Portability, Performance, and Persistence](portability_performance_and_persistence/readme.md) |
|  10:20 - 11:50 | Develop locally: Participants will learn to build and test containers on their local computer. (Hands-on 40 minutes) |
|  11:00 -  11:30 | Break   | 
|  11:30 - 11:45 | Deploy to the cloud: Using the XSEDE Jetstream resource, participants will create a virtual machine and deploy their containers to it. (30 minutes) |
|  11:45 - 12:00 | Scale to HPC: Participants will convert their Docker containers to Singularity and run them on an HPC resource at TACC. They will look at code performance between their local machine, the cloud, running in a container on HPC hardware, and running without a container on HPC hardware. We will discuss the pros and cons of containers and different container technologies. (40 minutes) |
|  12:00 - 12:30 | Implications and Resources: Summarize results. Look at container repositories for scientific codes. Discuss applications of the technology(20 minutes) |

B. Session II  

|Time           | Topic                                                       |
|---------------|-------------------------------------------------------------|
|  13:30 - 14:00 | [Discuss the app lifecycle and challenges with distribution, provenance, and reproducibility](portability_performance_and_persistence/portability.md) (20 minutes) |
|  14:00 - 14:30 | Agave as a Gateway Drug: A survey of alternative frameworks available in the Science-as-a-Service world and the trade offs associated with each one. (30 min) |
|  14:30 - 15:00 | HPC from the Web using Agave: Register HPC Systems as Agave systems and explore the data management and collaboration capabilities it provides. (40 minutes) |
|  15:00 -  15:30 | Break   | 
|  10:20 - 10:50 | Science Apps: Turn the container from the morning session into a shareable, web accessible app. Run the app through the API and observe execution on the host machine. Look at the metadata and version information captured by the platform. (30 minutes) |
|  10:20 - 10:50 | Collaborate Anywhere: Turn the container from the morning session into a shareable, web accessible app. Run the app through the API and observe execution on the host machine. Look at the metadata and version information captured by the platform. (30 minutes) |
|  10:20 - 10:50 | Future Possibilities: Some remarks on where containerization and Science-as-a-Service are going. This will include future plans for the Agave Platform. (30 min) |


## Prequisites

1. A decent text editor and knowledge to use it
2. Passing familiarity with Bash and UNIX-like filesystems
3. A good network connection

## Resources
* [Agave API website](https://agaveapi.co)
* [Agave Developer Documentation](http://developer.agaveapi.co)
* [Agave Jupyter Hub](https://jupyter.agaveapi.co)
* [Agave ToGo](https://deardooley.github.io/agave-togo/auth)
* [Slack Channel](https://slackin.agaveapi.co/)