# Apps and jobs 
---

Once you have storage and execution systems registered with Agave, you are ready to to build and use apps.  An Agave App is versioned, containerized executable that runs on a specific execution system.  So, for example, if you have multiple versions of a software package on a system, you would register each version as its own app.  Likewise, for a software package available on multiple execution systems, each system would use a different Agave app to use that software. 

Agave keeps a registry of apps that you can list and search.  The Apps service provides permissions, validation, archiving, and revision information about each app in addition to the usual discovery capability.

## Registering an app  

Registering an app with the Apps service is conceptually simple. Just describe your app as a JSON document and POST it to the Apps service. Historically, this has actually been the hardest part for new users to figure out. So, to ease the process, we've created a couple tools that you can use to define your apps. The first is the <a href="http://agaveplatform.org/tools/app-builder/" title="App Builder">App Builder</a> page. On this page you will find a form-driven wizard that you can fill out generate the JSON description for your app. Once created, you can POST the JSON directly to the Apps service. If you are new to app registration, this is a great place to start because it shrinks the learning curve involved in defining your app.

The second tool is the <a href="https://bitbucket.org/taccaci/agave-samples/" title="Agave Samples Repository" target="_blank">Agave Samples</a> project. The Agave Samples project is a set of sample data that cover a lot of use cases. The project contains several app definitions ranging in complexity from a trivial no-parameter, no-argument hello world, to a complex multi-input application with multiple parameter types. The Agave Samples project is a great place to start when building your app by hand because it draws on the experiences of many successful application publishers. 

## Packaging your app  

Agave apps are bundled into a directory and organized in a way that Agave can properly invoke it. Though there is plenty of opportunity to establish your own conventions, at the very least, your application folder should have the following in it:

* An execution script that creates and executes an instance of the application. We refer to this as the <em>wrapper template</em> throughout the documentation. For the sake of maintainability, it should be named something simple and intuitive like `wrapper.sh`. More on this in the next section. 
* A library subdirectory: This contains all scripts, non-standard dependencies, binaries needed to execute an instance of the application.  
* A test directory containing a script named something simple and intuitive like `test.sh`, along with any sample data needed to evaluating whether the application can be executed in a current command-line environment. It should exit with a status of 0 on success when executed on the command line. A simple way to create your test script is to create a script that sets some sensible default values for your app's inputs and parameters and then call your wrapper template. 

The resulting minimal app bundle would look something like the following:

```always
pyplot-0.1.0
|- app.json
|+ lib
 |- main.py
|+ test
 |- test.sh
|- wrapper.sh
```

## An example app

### The app description

Below is a simple app description that takes a single file and no parameters as input and creates one file as output.  The app description we give to Agave can be simpler than what is below, but a number of optional fields were included to demonstrate their use.

```json
{  
   "name":"wc-uhhpc-USERNAME",
   "version":"1.0",
   "label":"Linux wc utility",
   "shortDescription":"Count words in a file",
   "longDescription":"",
   "tags":[ "gnu", "textutils" ],
   "deploymentSystem":"uhhpc1-lustre-USERNAME",
   "deploymentPath":"apps/wc/",
   "templatePath":"/wrapper.sh",
   "testPath":"/test.sh",
   "executionSystem":"uhhpc1-exec-USERNAME",
   "executionType":"HPC",
   "parallelism":"SERIAL",
   "modules":[],
   "inputs":[  
      {  
         "id":"query1",
         "details":{  
            "label":"File to count words in: ",
            "description":"",
            "argument":null,
            "showArgument":false,
         },
         "semantics":{  
            "fileTypes":[ "text-0" ],
            "minCardinality":1,
            "ontology":[ "http://sswapmeet.sswap.info/util/TextDocument" ]
         },
         "value":{  
            "default":"test/input.txt",
            "order":0,
            "required":false,
            "validator":"",
            "visible":true
         }
      }
   ],
   "parameters":[],
   "outputs":[  
      {  
         "id":"outputWC",
         "details":{  
            "description":"Results of WC",
            "label":"Text file"
         },
         "semantics":{  
            "maxCardinality":1,
            "minCardinality":1,
            "ontology":[ "http://sswapmeet.sswap.info/util/TextDocument" ]
         },
         "value":{  
            "default":"wc_out.txt",
            "validator":""
         }
      }
   ]
}
```

Looking at some of the important keywords:
* **name** - Apps are given an ID by combining the "name" and "version". That combination must be unique across the entire Agave tenant, so unless you are an admin creating public system, you should probably put your username somewhere in there, and it's often useful to have the system name somehow referenced there too. You shouldn't use spaces in the name.
* **version** - This should be the version of the software package that you are wrapping.  If you end up updating your app description later on, Agave will keep track of the app revision separately, so there is no need to reflect that here.
* **deploymentSystem** - The data storage system where you keep the app assets, such as the wrapper script, test script, etc.  App assets are not stored on the execution system where they run.  For provenance and reproducibility, Agave requires that you keep them on a storage system.
* **deploymentPath** - the directory on the deploymentSystem where the app bundle is located
* **templatePath** - This template is what Agave uses to run your app.  The path you specify here is relative to the deploymentPath
* **testPath** - The intention here is that you include a testcase inside of your app bundle.
* **argument** - In combination with "showArgument", the "argument" keyword is a convenience that lets you build up commandline arguments in your wrapper script.
* **Cardinality** - Sets the min and max number of files you can give for inputs and outputs.  A "maxCardinality" of -1 will accept an unlimited number of files.

### Wrapper script

We have set this up to have a minimal wrapper script:

```sh
wc ${query1} > wc_out.txt
```

Within a wrapper script, you can reference the ID of any Agave input or parameter from the app description.  Before executing a wrapper script, Agave will look for the these references and substitute in whatever was that value was.  This will make more sense once we start running jobs, but this is the way we connect what you tell the Agave API that you want to do and what actually runs on the execution system.  The other thing Agave will do with the wrapper script is prepend all the scheduler information necessary to run the script on the execution system.

## Registering an app

Once you have an application bundle ready to go, you can register the app with the following CLI command:

```
apps-addupdate -F app.json
```

Agave will check the app description, look for the app bundle on the deploymentSystem, and if everything passes, make it available to run jobs against

## Running a job

Once you have at least one app registered, you can start running jobs.  To run a job, Agave just needs to know what app you want to run and what inputs and parameters you want to use.  There are number of other optional features, which are explained in detail in the [Agave Job Management Tutorial](http://agaveplatform.org/documentation/tutorials/job-management-tutorial/)

```
{
  "name":"test-wc-job",
  "appId": "wc-uhhpc-USERNAME-1.0",
  "executionSystem": "uhhpc1-exec-USERNAME",
  "batchQueue": "sb.q",
  "maxRunTime": "00:10:00",
  "nodeCount": 1,
  "processorsPerNode": 1,
  "archive": true,
  "archiveSystem": "uhhpc1-lustre-USERNAME",
  "archivePath": "./test-wc-job-out/",
  "inputs": {
    "query1": "agave://uhhpc1-lustre-USERNAME/input1.txt"
  },
  "parameters": {
  },
  "notifications": [
    {
      "url":"your@email.edu",
      "event":"FINISHED",
      "persistent":false
    },
    {
      "url":"your@email.edu",
      "event":"FAILED",
      "persistent":false
    }
  ]
}
```

* **name** - Just the name of the job for your own record keeping
* **appId** - This must match the app that you registered
* **archive** - If you set it to false, it will leave the temporary directory and output in place on the execution system  If set to true, Agave will gather up any new files created during the job and archive them at the archivePath on the archiveSystem.
* **notifications** - A really handy way to get notified when your job has finished.  Agave supports email, but also through [webhooks](http://agaveplatform.org/documentation/tutorials/job-management-tutorial/#webhooks), which becomes very powerful if building out front-end apps that consume this information.

Note that you can specify which queue to use as well as runtime limits in your job.  If those are absent, Agave falls back to whatever was listed in the app description (also optional).  If that app doesn't specify, then it falls back to the defaults given for the execution system.

Once you have your job.json file ready, you can submit a job using this command:

```
jobs-submit -F job.json
```

If you have direct access to the system where you are running the job, it is fun to watch it progress through on the system itself.  You can also use Agave to track job progress by using the job ID that it gave you.  If you didn't get it when you ran the job, you can look at all your job IDs with this command:

```
jobs-list
```

To see the history of a single job, use the jobs-history command with your job ID as the only argument.

```
jobs-history <JOB ID>
```

## More Resources

Building Agave applications can be very rewarding way to share your code with your colleagues and the world. This is a very simple example. If you are interested to learn more, please check out the [App Management Tutorial](http://agaveplatform.org/documentation/tutorials/app-management-tutorial/) on the Agave Developer Portal.

Example JSON descriptions are also available here: https://bitbucket.org/taccaci/agave-samples