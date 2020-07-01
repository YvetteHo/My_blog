FROM alpine
WORKDIR /app

ADD . /app
RUN rm -r static && rm db.sqlite3 

RUN apk add --no-cache python3 python3-dev sqlite zlib-dev jpeg-dev gcc libc-dev linux-headers py3-pip \
    && pip3 install uwsgi \
    && pip3 install -r requirements.txt
    && apk del python3-dev zlib-dev jpeg-dev libc-dev linux-headers py3-pip

RUN python3 manage.py collectstatic

CMD ["uwsgi", "--chdir", "/app", "-w", "cat.wsgi", "--socket", "/run/uwsgi/blog.sock", "--chmod=666"]
