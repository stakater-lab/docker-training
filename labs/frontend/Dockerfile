FROM python:2.7.15-alpine
RUN pip install --upgrade pip flask requests
COPY hello-world-front.py /tmp/hello-world-front.py
CMD ["python","/tmp/hello-world-front.py"]
