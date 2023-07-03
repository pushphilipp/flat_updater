FROM node:20 
RUN apt-get update && apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

WORKDIR /flat_updater

#Copy all files to the container
COPY . .

RUN npm install 
#Start Container by running the NodeJS script
CMD ["node", "wg_updater.js"]
