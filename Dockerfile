FROM alpine:latest

#install python and pip 
RUN apk app --no-cache --update python3 py3-pip bash
ADD ./Gender_Classification_Deployment/requirements.txt /tmp/requirements.txt

#install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

ADD ./Gender_Classification_Deployment /opt/Gender_Classification_Deployment
WORKDIR /opt/Gender_Classification_Deployment

# Run image as non root user
RUN adduser -D myuser
USER myuser

#run the app
CMD gunicorn --bind 0.0.0.0:$PORT wsgi



# FROM python:3.7-slim-buster
# WORKDIR /Gender_Classification_Deployment
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# RUN pip install opencv-python-headless
# COPY . .

# CMD [ "python3", "-m" , "app.py"]