# Yolov7 Microservice

A microservice predict objects in image using yolov7 model.

## 1. Introduction

In this repository, I use yolov7 model with ONNX format to predict objects in image and use FlaskAPI to write simple microservice to return result after model's prediction.

## 2. Prerequisites

Step 0: Install relating packages

```shell
python -m pip install -r requirements.txt
```

Step 1: Convert yolov7.pt to yolov7.onnx. (This step is introduced at Export section in yolov7 repository [link](https://github.com/WongKinYiu/yolov7))

Step 2: Create model folder and copy yolov7.onnx

```shell
cd src
mkdir model
```

## 3. Usage

Run command to start service

```shell
python src/app.py
```

## 4. Docker
In this repo, I wrote Dockerfile to build docker image. You can run following command to build it.

```shell
docker build --tag [NAME OF IMAGE]:[TAG VERSION] --network host .
```

After that, you run container from built image

```shell
docker run -it -d -p 9999:9999 --name [NAME OF CONATINER] [IMAGE ID]
```
