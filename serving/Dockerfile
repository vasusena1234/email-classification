FROM python:3.9-slim

# Create app structure
WORKDIR /app/src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY main.py .

# Start the Flask app
CMD ["gunicorn", "--chdir", "/app/src", "main:app", "-b", "0.0.0.0:9001"]
