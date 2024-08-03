# Use the official Python image as the base image
FROM python:3.12-slim

# Install cron
RUN apt-get update && apt-get install -y cron

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set environment variables
ENV CREDENTIALS_PATH=/.credentials
ENV FILE_LOGGING_LEVEL=INFO
ENV CRON_SCHEDULE="* * * * *"

# Set the entrypoint script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
