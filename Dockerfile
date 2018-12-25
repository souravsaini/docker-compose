#Base Image
FROM ubuntu:latest

#Metadata
MAINTAINER Sourav Saini "souravsaini972@gmail.com"

#System updates
RUN apt-get update -y && apt-get upgrade -y

#Python basic packages installation
RUN apt-get install -y python-pip python-dev build-essential

#Default work directory. By default, container will point to workdir path when run.
WORKDIR /usr/app

#Copy requirements file related to project
COPY requirements.txt .

#Install project related packages. Keep it isolated from application code so that it downloads and installs  only once (will be cached)
RUN pip install -r requirements.txt

#Make folder structure and copy application code
RUN mkdir app
COPY app app/
COPY ["microblog.py", "./"]

#Set environment variable so that flask knows the default file to look for at the time of run.
ENV FLASK_APP=microblog.py

#Exposed port 5000 for port forwarding
EXPOSE 5000

#Command to run the application
CMD [ "flask", "run" ]
