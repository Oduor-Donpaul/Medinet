#Use official Python runtime as a parent image
FROM python:3.9

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set working directory
WORKDIR /app

#Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN ls -l /app

#Copy project files into the container
COPY . .



#Expose port
EXPOSE 8000

#Run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

