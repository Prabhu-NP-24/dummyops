# First Stage: Build Stage
FROM node:14-alpine AS build
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
# Adjust this line based on your project structure
RUN npm run build  

# Second Stage: Run Stage
FROM node:14-alpine
WORKDIR /usr/src/app
# Adjust this line based on your project structure
COPY --from=build /usr/src/app /usr/src/app  
EXPOSE 3000
CMD ["npm", "start"]
