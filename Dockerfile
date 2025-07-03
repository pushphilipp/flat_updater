FROM selenium/standalone-chrome:latest

RUN sudo apt-get update
#Install Python 
RUN sudo apt-get install -y python3 python3-pip
RUN pip3 install selenium

COPY ./flat_updater.py /opt/bin/flat_updater.py
COPY ./start.sh /opt/bin/start.sh
COPY ./config.json /opt/bin/config.json
RUN sudo chmod +x /opt/bin/start.sh


CMD [ "/bin/bash", "/opt/bin/start.sh" ]