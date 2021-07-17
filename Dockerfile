FROM python:3.7-slim-buster
# FROM ubuntu
WORKDIR /Gender_Classification_Deployment
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install opencv-python-headless
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]