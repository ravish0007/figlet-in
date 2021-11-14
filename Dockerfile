FROM debian:latest

RUN apt-get -y update
RUN apt-get -y install sudo python3 python3-pip

COPY . /figlet-in

WORKDIR /figlet-in

RUN bash setup.sh


