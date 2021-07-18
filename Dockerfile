FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install opencv-python-headless
ENTRYPOINT ["python"]
CMD ["app.py"]
# FROM python:3.7-slim-buster
# WORKDIR /Gender_Classification_Deployment
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# RUN pip install opencv-python-headless
# COPY . .

# CMD [ "python3", "-m" , "app.py"]