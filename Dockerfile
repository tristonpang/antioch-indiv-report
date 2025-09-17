# Use official Python image
FROM python:3.11-slim

# Install system dependencies for Kaleido/Plotly
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libnss3 libfontconfig1 libxss1 libasound2 libxtst6 libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN plotly_get_chrome
RUN apt update && apt-get install libnss3 libatk-bridge2.0-0 libcups2 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libxkbcommon0 libpango-1.0-0 libcairo2 libasound2

# Expose port (DigitalOcean expects 8080)
EXPOSE 8080

# Set environment variable for Flask (if using Flask)
ENV PORT=8080

# Set the default command (update this to your actual entrypoint)
# For Flask:
# CMD ["gunicorn", "your_flask_app:app", "--bind", "0.0.0.0:8080"]
# For your script:
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]