FROM alpine
WORKDIR /app

RUN apk add --no-cache python3 python3-dev sqlite zlib-dev jpeg-dev gcc libc-dev linux-headers py3-pip
RUN pip3 install uwsgi

ADD . /app
RUN pip3 install -r requirements.txt

EXPOSE 80
CMD ["uwsgi", "--chdir", "/app", "-w", "cat.wsgi", "--socket", "/run/uwsgi/blog.sock", "--chmod=666"]
