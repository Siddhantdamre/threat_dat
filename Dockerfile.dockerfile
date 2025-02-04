# Use an official Node.js runtime as a parent image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose port 3000 for React
EXPOSE 3000

# Command to run the React app
CMD ["npm", "start"]
