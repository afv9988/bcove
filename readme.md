# bcove CDN Log Aggregator

This is a web aplication for excecute an analysis of log files, showing the relevant information in tables and charts.

The information of the log file is procesed into a python dictionaries, trying to use only libraries includes in python by default for reduce compatibility isues.

Main functions of the aplication are isolated from the framework specific functionalities, in order to reduce the dependence in case of switch to another framework.

## Web based

This project use Python3 and web2py framework for web and REST services, also is deploiment into a docker container: [Docker container](https://hub.docker.com/repository/docker/afdev9988/w2p) 

CI -CD using TravisCI for run unitary tests trigguered o comit to this repository

## Create files and folders
