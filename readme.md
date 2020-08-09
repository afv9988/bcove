
# bcove CDN Log Aggregator

![alt text](https://raw.githubusercontent.com/afv9988/bcove/master/static/images/FrontEnd.png)

This is a web aplication for excecute an analysis of log files, showing the relevant information in charts and tables.

The information of log file is procesed into a python dictionaries, trying to use only libraries includes in python by default for reduce compatibility issues.


## Web based

This project use Python3 and Web2py framework for web and REST services, this is accesible via HTTPS. 

Main functions of the aplication are isolated from the framework specific functionalities, in order to reduce the dependence in case of switch to another framework.

deploiment into a docker container: 

For CI -CD use Travis CI for run unitary and integration test, trigguered in commit repository, also deploy the new build to Build_30Build_30 you can seek the status of deployments [here](https://travis-ci.org/github/afv9988/bcove).

![alt text](https://travis-ci.org/afv9988/bcove.svg?branch=master)

## Deploy with yalm files

You can use the yaml this files for deploy the application to Kubernetes instance:

[Deploy](https://raw.githubusercontent.com/afv9988/bcove/master/kubernetes/deployment.yaml).
[Service](https://raw.githubusercontent.com/afv9988/bcove/master/kubernetes/service.yaml).
