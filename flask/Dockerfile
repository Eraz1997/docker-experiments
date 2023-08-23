FROM python:2.7-slim

WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org Flask
ENV NAME ENRS
CMD ["python", "app.py"]
