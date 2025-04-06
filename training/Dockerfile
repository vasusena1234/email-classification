# Use Python 3.12 for consistency
FROM python:3.12

# Create standard app structure
RUN mkdir -p /app/src/
RUN mkdir -p /app/data/
RUN mkdir -p /app/model/

# Copy source files
COPY requirements.txt /app/src/
COPY main.py /app/src/

# Install Python dependencies
RUN pip3 install -r /app/src/requirements.txt

# Set proper permissions for SAP AI Core
RUN chgrp -R 65534 /app && \
    chmod -R 777 /app
