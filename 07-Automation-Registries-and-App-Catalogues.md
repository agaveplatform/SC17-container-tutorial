# Automation
* Agave
* CI/CD
* Image publishing

## Building
 Continuous integration servers are the workhorse of our automation solution. They handle image building, testing, tagging, promotion, release, log management, access control, and publishing. We will leverage [Jenkins](https://jenkins.io) to handle our CI needs. We could just as easily leverage TravisCI, CircleCI, Gitlab, Bitbucket Pipelines, or a multitude of other excellent CI products and services. We chose Jenkins because it is arguably the leading open source CI solution, has a large, active user and developer community behind it, and is commonly used for building and publishing container images.

 We have already stood up a Jenkins server on our tutorial build server. Commands to register your repositories for automated builds are present in your environment. You can authenticate to the server with your Agave credentials.

 > A list of alternative CI servers is available in the DevOps section of the [References](99-References.md#DevOps).  

## Testing
Whatever mechanism you are using for testing, if you have a test suite for your application (an you should), then it should run prior to every build of your image. The same mechanism you used to build your image will be used to run the test suite. We will add two additional files to our funwave repository, `Dockerfile.test` and `Singularity.test`. These two files will be built after the initial image build. Successful builds will indicate a successful test run. Anything else indicates failure.

Dockerfile.test  **[TODO]** @stevenrbrandt please edit the Dockerfile to run the funwave test suite here  

```
...
RUN make clean && \
    make test
...    
```

Singularity.test  **[TODO]** @stevenrbrandt please edit the Singularity file to run the funwave test suite here  

```
...
%tests
  make clean
  make test
...
```  

> Further information on automated testing with Docker and Singularity can be found in the [References](99-References.md#DevOps).  

## Versioning, tagging, an naming  
Before you put automation in place, you should stop to think about how you will version the images built upon each push to your code repository. By default, the automation we set in place here will build and tag your images with the branch, commit hash, and tag of the commit that triggered the build. In doing so, you will have a clear connection that users can identify between the container that runs, the image it came from, the build that triggered the image, the commit that triggered the build, and the user who pushed the commit.

There are situations where you may prefer to create greater or fewer tags for a given image. For instance, if you have a formal release branch, you may prefer to skip building everything but the master branch. In that case, you may prefer skipping branch tagging and prefer to use git tags as your image tag. (Even in this situation, we still recommend keeping the git hash tag to maintain transparency to your users.)  

Applications like FUNWAVE-TVD have a relatively easy time picking a name for their image. Projects like BIDS, which represent dozens of codes and multiple pipelines, have a much more difficult time. If you plan on making your image publicly available, a good rule of thumb is to err on the side of communication over accuracy. You can always clarify your name choice 


## Pushing, polling, and webhooks

```
repositories-list
repositories-addupdate
repositories-delete
{
  "url": "https://github.com/agaveplatform/sandbox",
  "poll": true,
  "builds": [
    {
      "branch"


```

# Dual image builds

## Sample pipeline

## Validating images  

# Registries

## Public vs private

## Caching images

## Mirroring

# App Catalogues  

## Finding an audience

## Building trust

## Setting expectations

## Tracking usage
