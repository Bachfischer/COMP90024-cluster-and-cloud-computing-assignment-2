FROM node:13.12.0-alpine as builder

WORKDIR /app
COPY . .
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent
RUN yarn run build


FROM node:13.12.0-alpine
RUN yarn global add serve
WORKDIR /app
COPY --from=builder /app/build .
EXPOSE 4000
CMD ["serve", "-p","4000","-s","."]

