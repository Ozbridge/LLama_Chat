# syntax=docker/dockerfile:1

FROM ubuntu:latest

WORKDIR /app
COPY . .
RUN set -xe
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 
RUN make
CMD ["/app/server", "-m",  "models/13B/llama-2-13b-chat.Q2_K.gguf", "-c", "2048", "--host", "0.0.0.0"]
EXPOSE 8080