# bcove CDN Log Aggregator

This is a web aplication for excecute an analysis of log files, showing the relevant information in tables and charts.

The information of the log file is procesed into a python dictionaries, trying to use only libraries includes in python by default for reduce compatibility isues.

Main functions of the aplication are isolated from the framework specific functionalities, in order to reduce the dependence in case of switch to another framework.

## Web based

This project use Python3 and web2py framework for web and REST services, is deploiment into a docker container: [Docker container](https://hub.docker.com/repository/docker/afdev9988/w2p) 

For CI -CD use TravisCI for run unitary tests trigguered in comit to this repository, you can seek the status [here](https://travis-ci.org/github/afv9988/bcove)

## Create files and folders
