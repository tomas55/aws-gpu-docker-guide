#!/bin/bash

IMAGE_NAME=ml-gpu-example
REGISTRY_URL=755889831808.dkr.ecr.eu-central-1.amazonaws.com

docker build -t $IMAGE_NAME . 
docker tag $IMAGE_NAME $REGISTRY_URL/$IMAGE_NAME
docker push $REGISTRY_URL/$IMAGE_NAME