FROM python:3.7-slim-buster
WORKDIR /Gender_Classification_Deployment
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install opencv-python-headless
COPY . .

CMD [ "python3", "-m" , "app.py"]