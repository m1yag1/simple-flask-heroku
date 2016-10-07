FROM ubuntu:14.04.1

RUN apt-get update && apt-get install -yq \
  python-dev \
  python-pip \
  libssl-dev \
  libffi-dev \
  build-essential

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -q -r requirements.txt

CMD gunicorn app:app --bind 0.0.0.0:5000
