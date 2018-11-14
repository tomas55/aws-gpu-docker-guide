FROM tensorflow/tensorflow:1.11.0-gpu-py3

RUN pip install boto3

WORKDIR /app
COPY src/worker.py ./
CMD ["python","worker.py"]