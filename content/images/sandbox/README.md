# Agave Tutorial user sandbox

This is a ssh-enabled single-user sandbox for use in user trainings. It provides a user login environment with a common build environment sufficient for container and/or native builds.  


## Requirements

* Docker >= 1.11
* Docker Compose >= 1.7
 
## Building

```
docker build -t agaveplatform/ssh-sandbox .
```  

## Running

```
docker run -d --name sandbox -p 10022:22 agaveplatform/ssh-sandbox