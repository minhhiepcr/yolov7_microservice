FROM python:3.8

ADD . .

COPY ./requirements.txt ./requirements.txt

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN python -m pip install -r requirements.txt

CMD ["python3", "src/app.py"]