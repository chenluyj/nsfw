#!/usr/bin/env bash
#docker pull tensorflow/serving
MODEL_NAME=nsfw
MODEL_BASE_PATH=`pwd`/data/models/$MODEL_NAME
docker run -t --rm -p 8501:8501 \
    -v "$MODEL_BASE_PATH:/models/$MODEL_NAME" \
    -e MODEL_NAME=$MODEL_NAME \
    tensorflow/serving &
