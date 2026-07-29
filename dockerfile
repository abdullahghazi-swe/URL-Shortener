FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1

# Show Python logs immediately
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Tell Docker the application listens on port 8000
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "url.wsgi:application", "--bind", "0.0.0.0:8000"]