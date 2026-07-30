FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1

# Show Python logs immediately
ENV PYTHONUNBUFFERED=1

ENV DJANGO_SETTINGS_MODULE=url.settings.production

# Working directory inside the container
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

RUN chmod +x entrypoint.sh

# Tell Docker the application listens on port 8000
EXPOSE 8000

# Start Gunicorn
ENTRYPOINT [ "./entrypoint.sh" ]