# HPC via HTTP: Portable, Scalable Computing using App Containers and the Agave API

Supercomputing matters. So does user experience. Standing between the mainstream adoption of supercomputing and a new generation of users is the reality that the entry cost to using these systems, both in terms of dollars and in time spent learning the technology, has not significantly changed in the last 20 years. The rise of cloud computing only complicates the learning curve further. Over the last 6 years, the authors have been addressing this gap through the development of a Science-as-a-Service platform enabling users to go from their desktop, to their local data center, to the cloud, and back without sacrificing their existing tool chain or user experience.

In this tutorial, we combine best practices and lessons learned while on-boarding the last 70k new users to TACC’s data center through the Agave Platform. Participants will walk through the process of scaling their application from a local environment to the Jetstream academic cloud and to a high performance computing system at the Texas Advanced Computing Center. They will learn to use multiple container technologies to harmonize app execution between cloud and HPC resources, and they will learn to use modern APIs to orchestrate job execution, capture provenance information, and foster collaboration.


# Schedule

|Time           | Topic                                                       |
|---------------|-------------------------------------------------------------|
|  8:30 - 9:00 | [Overview and introductions](overview/readme.md): Introduce instructors and learners. Lay out learning objectives for the morning session. Present an overview of containers and Science-as-a-Service APIs (Presentation and Discussion; 30 minutes)|
|  9:00 - 9:20 | [Resources, Jupyter, Login](setup/readme.md) (hands-on)|
|  9:20 - 10:00 | [Code, Build, and Test](portability_performance_and_persistence/readme.md) |
|  9:20 - 9:40 | Checkout, build, run locally: Participants will learn to build and test containers on their local computer. (Hands-on 40 minutes) |
|  9:40 - 10:00 | Set up auto-build, commit/save code change, run local and remote via agave cli/skd |
|  10:00 - 10:30 | Break  |
|  10:30 - 10:45 | [Viewing simulation results, sharing, provenance](sharing/readme.md)  |
|  10:45 - 11:30 | [Packaging and publishing experimental runs, results and codes](publishing/readme.md)|
|  11:30 - 12:00 | [Scaling, benchmarking, future directions, homework](performance/readme.md) |

# Table of Contents

- 01: [Requirements and Preparation](01-Requirements-and-Preparation.md)
- 02: [Installation and Infrastructure](02-Installation-and-Infrastructure.md)
- 03: [Auth, Notebooks, and the Web Interface](03-Auth-Notebooks-and-Web-Console.md)
- 04: [SciOps and our Sample Application](04-SciOps-and-Sample-Application.md)
- 05: [Code, Build, and Run Locally](05-Code-Build-and-Run-Locally.md)
- 06: [Containerize Existing Applications](06-Containerize-Existing-Applications.md)
- 07: [Registries, Storage, and App Catalogues](07-Registries-Storage-and-App-Catalogues.md)
- 07: [Automation and Execution]()
* Agave
* CI/CD
* Image publishing
- 08: [Scaling and Portability]()
* Image caching
* Runtime environments
* Data scheduling
* Reproducibility anti-patterns
- 09: [Viewing simulation results, sharing, provenance]()
- 10: [Packaging and Publishing Experiments]()
- 11: [Benchmarking and Performance Considerations]()
- 12: [Functions, Microcodes, and Exascale]()
- 13: [Homework an Further Reading]()


- 04: [Resources and Hello, World!](04-Resources-and-Hello-World.md)
- 05: [Services, Routing and a Complete Example](05-Services-Routing-Complete-Example.md)
- 06: [Project Administration](06-Project-Administration.md)
- 08: [S2I Introduction](08-S2I-Introduction.md)




- 10: [Wiring Components](10-Wiring-Components.md)


- 11: [Rollback/Activate and Code Lifecycle](11-Rollback-Activate-Lifecycle.md)
- 12: [PHP Application Example With
    Storage](12-PHP-Application-Example-With-Storage.md)
- 13: [Customized Build and Run
    Processes](13-Customized-Build-and-Run-Processes.md)
- 14: [Lifecycle Pre and Post Deployment
    Hooks](14-Lifecycle-Pre-and-Post-Deployment-Hooks.md)
- 15: [JBoss EAP Example](15-JBoss-EAP-Example.md)

- 90: [Appendix A](90-Appendix-A.md)
- 99: [References](99-References.md)
