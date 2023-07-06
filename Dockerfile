FROM browserless/chrome

WORKDIR /flat_updater
COPY ./wg_updater.js ./wg_updater.js
COPY ./settings/config.js ./settings/config.js
COPY ./package.json ./package.json
COPY ./package-lock.json ./package-lock.json
# Check chrome version
RUN sudo npm install 
#Start Container by running the NodeJS script
CMD ["node", "wg_updater.js"]
