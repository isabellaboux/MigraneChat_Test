FROM python:3.13-slim

# Install system dependencies (FFmpeg needed for Whisper audio processing)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy dependency file first (for better caching)
COPY pyproject.toml .

# Copy the main application code
COPY main.py .

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Expose port 8000 for the web server
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]