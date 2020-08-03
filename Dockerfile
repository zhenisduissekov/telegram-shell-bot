FROM ubuntu:18.04

COPY . /opt
WORKDIR /opt
RUN apt update -y
RUN apt install -y curl

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*



RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb


RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.8
RUN apt install -y python3-pip
RUN pip3 install pyyaml
RUN pip3 install configparser
RUN pip3 install colorlog
RUN pip3 install Pillow
RUN pip3 install pytz
RUN pip3 install pyTelegramBotAPI
CMD /opt/main.py
