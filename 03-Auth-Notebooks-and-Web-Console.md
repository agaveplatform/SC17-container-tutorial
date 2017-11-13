# Jupyter environment

## Custom Kernels
Your Jupyter server has multiple kernels available for use right away. We have preconfigured them with several useful libraries and tools to help users get up and running with common tasks easier. Additionally, we have bundled in Agave CLI and Python SDK into the Bash and Python2 kernels respectively. Both kernels are pre-authenticated with valid Agave auth tokens that you can use to begin interacting with the Agave Platform right away.


## Shared file system
Your home directory on the Jupyter server is shared with your sandbox, so you can safely copy data between the two environments quickly and easily.

## Web console  
Jupyter contains a web terminal that can be used to access your sandbox environment or interact with the Jupyter container itself. To login to your sandbox from the Jupyter web terminal, simply run the following command:  

```
ssh sandbox
```

## Pre-authenticated API access
A valid Agave auth token has been placed on your system for you. If you are using the Bash or Python2 kernels, this token will be picked up automatically and refreshed as needed
## Tutorial notebooks

## Extras
Inside of the `examples` directory, you will find several notebooks to help you learn more about the Agave platform, containers, and SciOps. We leave these for you to follow after the tutorial.

## Sandbox environment
The sandbox has the following pre-installed:
* [TODO] @stevenrbrandt please review
* build-essential
* gfortran

## Sample application code
The sample code for this project is already present in `~/funwave-tvd`.

## Container runtimes
Docker and Singularity are both preinstalled in the Sandbox. Private registries for both container runtimes are hosted on `build.tutorial.public.agaveplatform.org`. You may authenticate with your Agave credentials.  

<span style='color:red'>Is this a browser or ssh login? What does the student do after logging in? Look at the source files? Trigger a build?</span>

## Agave CLI
The Agave CLI is available in your sandbox `~/src/agave-cli` directory. The commands are already present in your environment `$PATH`.

## Shared file system
Your home directory on the Jupyter server is shared with your sandbox, so you can safely copy data between the two environments quickly and easily.

## Accessibility
To login to the sandbox from outside the Jupyter server, use the fully qualified domain name. You can obtain valid ssh keys from the `~/.ssh` director of your Jupyter server.

```
ssh -i /path/to/private/key.pem -p 10022 jovyan@$VM_IPADDRESS
```
