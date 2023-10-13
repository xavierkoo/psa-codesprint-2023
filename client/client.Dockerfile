FROM node:alpine

RUN npm install -g http-server

# set the working direction
WORKDIR /app

# install app dependencies
COPY package*.json ./

# Fix permissions for packages
# RUN npm config set unsafe-perm true
RUN npm install

# Bundle app source
COPY . ./

EXPOSE 8080

CMD [ "npm", "run", "dev" ] 