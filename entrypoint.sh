#!/bin/bash

# Print environment variables for debugging
echo "CRON_SCHEDULE: $CRON_SCHEDULE"

# Change directory to /app
cd /app || exit

# Run the Python script immediately
/usr/local/bin/python main.py

# Create a crontab entry
echo "$CRON_SCHEDULE cd /app && /usr/local/bin/python main.py >> /var/log/cron.log 2>&1" > /etc/cron.d/my_cron

# Apply cron job
crontab /etc/cron.d/my_cron

# Give execution rights on the cron job
chmod 0644 /etc/cron.d/my_cron

# Create the log file to be able to run tail
touch /var/log/cron.log

# Start the cron daemon
cron

# Tail the log file to see cron job output
tail -f /var/log/cron.log
