FROM ubuntu:latest
MAINTAINER Blas Rodriguez Irizar "rodrigblas@gmail.com"

RUN apt-get update
RUN apt-get install -y python python-pip wget


RUN mkdir /bloomb
ADD requirements.txt /bloomb/requirements.txt
WORKDIR /bloomb

RUN pip install -r requirements.txt

EXPOSE 6060

ENTRYPOINT sh docker-entrypoint.sh
