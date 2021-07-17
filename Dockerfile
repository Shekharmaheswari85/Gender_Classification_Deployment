FROM python:3.7-slim-buster
# FROM ubuntu
WORKDIR /Gender_Classification_Deployment

COPY requirements.txt requirements.txt
# RUN apt-get update
# RUN apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0
# RUN apt-get update \
#   && apt-get install -y python3-pip python3-dev \
#   && cd /usr/local/bin \
#   && ln -s /usr/bin/python3 python \
#   && pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip install opencv-python-headless
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]