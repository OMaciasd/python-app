# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the image
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Expose the port 8000
EXPOSE 8000

# Specify the command to run the application
CMD ["python", "app.py"]
