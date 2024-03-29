# Use the official Python base image
FROM python:3.11.6

RUN mkdir -p /usr/src/app/static/

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8000
