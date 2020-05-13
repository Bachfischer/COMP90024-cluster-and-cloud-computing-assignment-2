FROM node:13.12.0-alpine 

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm cache clean --force && npm install --silent

COPY . /app
EXPOSE 8000


CMD ["npm","run","start"]

