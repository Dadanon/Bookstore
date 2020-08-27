# # Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set work directory
WORKDIR /Desktop

# Install dependencies
COPY Pipfile Pipfile.lock /Desktop/
RUN pip install pipenv; pipenv install --system

# Copy project
COPY . /Desktop/