FROM ubuntu:latest
MAINTAINER Sourav Saini "souravsaini972@gmail.com"
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir app
COPY app app/
COPY ["microblog.py", "./"]
ENV FLASK_APP=microblog.py
EXPOSE 5000
CMD [ "flask", "run" ]
