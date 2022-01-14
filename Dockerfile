# Pull base image
FROM python:3.8
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
COPY reqs.txt /code/
RUN pip install -r reqs.txt
# Copy project
COPY . /code/
EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]