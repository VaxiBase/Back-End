# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Install cron
RUN apt-get update && apt-get -y install cron vim

WORKDIR /app
COPY . /app

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

RUN /usr/bin/crontab /etc/cron.d/crontab

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["cron", "-f"]
