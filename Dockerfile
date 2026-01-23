FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# App directory
WORKDIR /app
COPY . /app

# Install Python requirements
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Start bot
CMD ["bash", "start"]
