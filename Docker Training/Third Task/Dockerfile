# # Get the base image
# FROM node:12-alpine

# # Create a working directory
# RUN mkdir -p /usr/src/app

# # Make it the working directory
# WORKDIR /usr/src/app

# # Copy the packages.json file and after installing copy everything to the working directory in one layer
# COPY package*.json ./
# RUN npm install
# COPY . /usr/src/app

# # Run the Nodejs app and expose port 3000
# CMD [ "node", "index.js" ]
# EXPOSE 3000

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