
# Managing systems
---

The Agave API provides a way to access and manage the data storage and compute resources you already use (or maybe the systems you want to use), but first you have to tell Agave where they are, how to login, and how to communicate with that system.  That is done by giving Agave a short JSON description for each system.  

## Storage Systems

Storage systems tell Agave where data resides.  You can store files for running compute jobs, archive results, share files with collaborators, and maintain copies of your Agave apps on storage systems.  Agave supports lots of communication protocols and the permissions models that go along with them, so you can work privately, collaborate with individuals, or provide an open community resource.  It's up to you.  Here is an example of a simple data storage system accessed via SFTP:

```json
{
  "id": "uhhpc1-lustre-USERNAME",
  "name": "UH HPC1 SFTP Lustre Storage System",
  "type": "STORAGE",
  "description": "UH HPC Lustre storage system using SFTP at the University of Hawaii",
  "site": "hawaii.edu/its/ci",
  "storage": {
    "host": "uhhpc1.its.hawaii.edu",
    "port": 22,
    "protocol": "SFTP",
    "rootDir": "/",
    "homeDir": "/lus/scratch/USERNAME",
    "auth": {
      "username": "USERNAME",
      "password": "CHANGME",
      "type": "PASSWORD"
    }
  }
}
```

Let's go through the key items one-by-one:
* **id** - this is the unique name that you will use with Agave to use your system.  It must be unique across the entire Agave tenant, so unless you are an admin creating public system, you should probably put your username somewhere in there. You shouldn't use spaces in the system ID.
* **name** - A human-readable name
* **type** - either STORAGE or EXECUTION.
* **site** - This field is just for logically grouping systems by the site where they are located.
* **rootDir** - If you specify an absolute path on this Agave system, it will always be relative to the rootDir that is set.  For private systems, it is commonly left as "/".  For public systems, it is commonly set to a subdirectory to hide the root level system directories and restrict what other users can see.
* **homeDir** - If you specify a relative path on this Agave system, it will always be relative to the homeDir that is set/
* **auth** - This block tells Agave how to login.  An Agave system always includes information on how to authenticate.
  * **type** - There are a number of options: APIKEYS, LOCAL, PAM, PASSWORD, SSHKEYS, or X509.  For this example, we are using PASSWORD, since it is the simplest and requires no setup, but setting up SSHKEYS (or one of the other methods if they fit) is better for a production context.  More info is here: http://agaveapi.co/documentation/tutorials/system-management-tutorial/#supported-data-and-authentication-protocols

### Hands-on

As a hands on exercise, register a data storage system that you use.  This could be a remote VM, a storage space on a cluster at a university, or something in the commercial cloud like an S3 bucket.  Other examples of storage systems are here: http://agaveapi.co/documentation/tutorials/system-management-tutorial/#storage-systems

---
## Execution Systems

Execution systems in Agave are very similar to storage systems.  They just have additional information for how to launch jobs.  In this example, we are using a HCP system, so we have to give scheduler and queue information.

```json
{
  "id": "uhhpc1-exec-USERNAME",
  "name": "UH ITS HPC SSH Execution Host",
  "status": "UP",
  "type": "EXECUTION",
  "description": "Execution system using ssh to submit jobs to the UH ITS HPC. By default, it uses the Sandbox queue.",
  "site": "hawaii.edu",
  "executionType": "HPC",
  "scheduler": "SLURM",
  "environment": null,
  "startupScript": "./bashrc",
  "maxSystemJobsPerUser": 10,
  "scratchDir": "/lus/scratch/USERNAME",
  "queues": [
    {
      "name": "sb.q",
      "maxJobs": 25,
      "maxUserJobs": 5,
      "maxNodes": 2,
      "maxMemoryPerNode": "120GB",
      "maxProcessorsPerNode": 20,
      "maxRequestedTime": "01:00:00",
      "customDirectives": null,
      "default": true
    },
    {
      "name": "community.q",
      "maxJobs": 25,
      "maxUserJobs": 5,
      "maxNodes": 5,
      "maxMemoryPerNode": "120GB",
      "maxProcessorsPerNode": 20,
      "maxRequestedTime": "72:00:00",
      "customDirectives": null,
      "default": true
    },
    {
      "name": "exclusive.q",
      "maxJobs": 25,
      "maxUserJobs": 5,
      "maxNodes": 5,
      "maxMemoryPerNode": "120GB",
      "maxProcessorsPerNode": 20,
      "maxRequestedTime": "72:00:00",
      "customDirectives": null,
      "default": true
    },
    {
      "name": "kill.q",
      "maxJobs": 25,
      "maxUserJobs": 5,
      "maxNodes": 5,
      "maxMemoryPerNode": "120GB",
      "maxProcessorsPerNode": 20,
      "maxRequestedTime": "72:00:00",
      "customDirectives": null,
      "default": true
    }
  ],
  "login": {
    "host": "uhhpc1.its.hawaii.edu",
    "port": 22,
    "protocol": "SSH",
    "auth": {
      "username": "USERNAME",
      "password": "CHANGEME",
      "type": "PASSWORD"
    }
  },
  "storage": {
    "host": "uhhpc1.its.hawaii.edu",
    "port": 22,
    "protocol": "SFTP",
    "rootDir": "/",
    "homeDir": "/home/USERNAME",
    "auth": {
      "username": "USERNAME",
      "password": "CHANGME",
      "type": "PASSWORD"
    }
  }
}
```

We covered what some of these keywords are in the storage systems section.  Below is some commentary on the new fields:

* **executionType** - Either HPC, Condor, or CLI.  Specifies how jobs should go into the system. HPC and Condor will leverage a batch scheduler. CLI will fork processes.
* **scheduler** - For HPC or CONDOR systems, Agave is "scheduler aware" and can use most popular schedulers to launch jobs on the system.  This field can be LSF, LOADLEVELER, PBS, SGE, CONDOR, FORK, COBALT, TORQUE, MOAB, SLURM, UNKNOWN. The type of batch scheduler available on the system.
* **environment** - List of key-value pairs that will be added to the Linux shell environment prior to execution of any command.
* **scratchDir** - Whenever Agave runs a job, it uses a temporary directory to cache any app assets or job data it needs to run the job.  This job directory will exist under the "scratchDir" that you set.  The path in this field will be resolved relative to the rootDir value in the storage config if it begins with a "/", and relative to the system homeDir otherwise.

Complete reference information is located here: http://agaveapi.co/documentation/tutorials/system-management-tutorial/#execution-systems

### Hands-on

As a hands on exercise, register an execution system that you use.  This could be a remote VM, a cluster at a university, or something in the commercial cloud.  Other examples of execution systems are here: http://agaveapi.co/documentation/tutorials/system-management-tutorial/#supported-data-and-authentication-protocols
