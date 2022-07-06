# 使用手册

## 编辑.env
```bash
MODEL_NAME=nsfw
MODEL_BASE_PATH={youPath}/data/models/nsfw
```


## docker-compose 方式启动
```bash
docker-compose up -d
```
## 测试
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"url":"https://qiniu.gongxueyun.com/upload/04a01ddfea80a171c152215f29212f59.jpg@wh256"}'  "http://127.0.0.1:8888/nsfw"
```
## 停止服务
```bash
docker-compose stop
```
## 删除镜像
```bash
docker-compose rm
```



----
# NSFW Model

This repo contains code for running Not Suitable for Work (NSFW) classification.

[online demo](http://ai.midday.me/)

## Usage

#### script 

```bash
python nsfw_predict.py /tmp/test/test.jpeg
```

result : 
```bash
{'class': 'sexy', 'probability': {'drawings': 0.008320281, 'hentai': 0.0011919827, 'neutral': 0.13077603, 'porn': 0.13146976, 'sexy': 0.72824186}}
```

can find the meaning of every label at repo [nsfw_data_scrapper](https://github.com/alexkimxyz/nsfw_data_scrapper)

#### Deploy by TensorFlow Serving

your have to install [Tensorflow Serving](https://www.tensorflow.org/serving/) first

start the server
```bash
./start_tensorflow_serving.sh
```

test server
```bash
python serving_client.py /tmp/test/test.jpeg
```


## Train

train code at [resnet](./resnet)

train a new model

1. convert source to tfrecord user ```convert_image_to_tfrecord.py```
2. train a model from scratch or fine tune

the model code copy from [Tensorflow offical model](https://github.com/tensorflow/models/tree/master/official/resnet)


## Data

you can find the detail at repo [nsfw_data_scrapper](https://github.com/alexkimxyz/nsfw_data_scrapper)




 
