FROM python:3.8-slim-buster
FROM ubuntu:20.04
WORKDIR /Gender_Classification_Deployment

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]