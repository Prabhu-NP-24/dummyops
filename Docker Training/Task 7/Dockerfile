# Convert this into a multi stage
# Stage 1 : Build stage
FROM node:12-alpine AS build
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . /usr/src/app/

# Stage 2 : Running Stage
FROM node:14-alpine
WORKDIR /usr/src/app
COPY --from=build /usr/src/app /usr/src/app
EXPOSE 3000
CMD [ "node", "index.js" ]