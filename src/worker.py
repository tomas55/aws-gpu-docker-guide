from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

import boto3
import json
import os

model = ResNet50(weights='imagenet')

bucket = boto3.resource('s3').Bucket('ml-gpu-example')
queue = boto3.resource('sqs', 'eu-central-1').get_queue_by_name(QueueName='example-gpu-queue')

def processImage(file):
  bucket.download_file(file, file)
  
  img = image.load_img(file, target_size=(224,224))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  preds = model.predict(x)
  print('Predicted:', decode_predictions(preds, top=3)[0])
 
  os.remove(file)

def startWorker():
  while True:
    for message in queue.receive_messages(VisibilityTimeout=8000, MaxNumberOfMessages=10):
      key = json.loads(message.body)['Records'][0]['s3']['object']['key']
      processImage(key)
      message.delete()

startWorker()
