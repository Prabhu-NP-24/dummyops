# Step 1 : Use a lightweight OS for the docker image
FROM node:14-alpine

# Step 2 : Set the working directory
WORKDIR /usr/src/app

# Step 3 : Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Step 4 : Install Dependencies
RUN npm install

# Step 5 : Copy all files to the app directory
COPY . .

# Step 6 : Expose port 8080
EXPOSE 8080

# Step 7 : Command to run
CMD [ "npm","install" ]