FROM python:3.6
LABEL maintainer = "nikit phadke"
RUN apt-get update
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt