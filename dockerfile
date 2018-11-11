FROM tensorflow/tensorflow:1.11.0-gpu-py3

RUN pip install boto3

WORKDIR /app
COPY src/worker.py ./
COPY images/select-ami.jpeg ./select-ami.jpeg

CMD ["python","worker.py"]