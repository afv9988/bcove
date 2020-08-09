
# bcove CDN Log Aggregator

![alt text](https://raw.githubusercontent.com/afv9988/bcove/master/static/images/FrontEnd.png)

This is a web aplication for excecute an analysis of log files, showing the relevant information in charts and tables.

The information of log file is procesed into a python dictionaries, trying to use only libraries includes in python by default for reduce compatibility issues.


## Web based

This project use Python3 and Web2py framework for web and REST services, this is accesible via HTTPS. Deployed into a Docker container.

Main functions of the aplication are isolated from the framework specific functionalities, in order to reduce the dependence in case of switch to another framework.

For CI-CD pipeline, this project use Travis CI for run unitary and integration tests, this are triggered when the Git repository receive a push request, also, deploy the new build to [Docker Hub](https://hub.docker.com/repository/docker/afdev9988/w2p) you can seek the status of deployments [here](https://travis-ci.org/github/afv9988/bcove).

![alt text](https://travis-ci.org/afv9988/bcove.svg?branch=master)

## Deploy in Kubernetes with yaml files

You can use this yaml files for deploy the application to Kubernetes instance:

[Deploy](https://raw.githubusercontent.com/afv9988/bcove/master/kubernetes/deployment.yaml)

[Service](https://raw.githubusercontent.com/afv9988/bcove/master/kubernetes/service.yaml)

After import the yaml files you can acces to application via:

[https://SERVER_IP:30000/](https://SERVER_IP:30000/)

## Links
Application: [https://afdev.ddns.net/](https://afdev.ddns.net/)

Kubernetes Intance: [https://afdev.ddns.net:10443/#/login](https://afdev.ddns.net:10443/#/login)
