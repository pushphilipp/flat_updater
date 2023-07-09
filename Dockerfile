FROM amd64/node:latest


WORKDIR /flat_updater
COPY ./wg_updater.js ./wg_updater.js
COPY ./settings/config.js ./settings/config.js

RUN apt update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome-stable_current_amd64.deb -y
RUN npm install selenium-webdriver -y
RUN npm install chromedriver -y
#Start Container by running the NodeJS script
CMD ["node", "wg_updater.js"]