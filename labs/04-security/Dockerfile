FROM python:2.7.15-alpine
RUN pip install --upgrade pip flask

HEALTHCHECK NONE

COPY hello-world-back.py /tmp/hello-world-back.py
CMD ["python","/tmp/hello-world-back.py"]
