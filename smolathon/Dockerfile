FROM python:3.10.5
WORKDIR /app
RUN apt-get update \
&& apt-get install -y python3-dev
RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

