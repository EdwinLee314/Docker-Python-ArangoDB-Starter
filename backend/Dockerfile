
# this is an official Python runtime, used as the parent image
FROM python:3.6-alpine3.7

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 5000 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
CMD ["python", "app.py"]

# docker run -p 5000:5000 --volume=/Users/edwin/project/eureka-backend:/app edwinlee314/flaskdock