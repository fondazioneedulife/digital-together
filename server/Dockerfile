FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

## add user
RUN adduser -D user
RUN chown -R user:user /server && chmod -R 755 /server

COPY server/requirements.txt server/requirements.txt

# RUN apk update 
# RUN apk add --virtual build-deps gcc python-dev musl-dev 
# RUN apk add postgresql-dev 
# RUN apk add netcat-openbsd
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

RUN pip3 install -r server/requirements.txt
USER user

COPY . .

EXPOSE 8000
# RUN python manage.py migrate
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

