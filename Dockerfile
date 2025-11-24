# Dockerfile
# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first for caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port that Next.js will run on
# EXPOSE 3000

# Start the Next.js application
# CMD ["npm", "run", "dev"]