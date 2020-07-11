# base image
FROM python:3-alpine

# install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2-binary \
    && apk del build-deps

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000



CMD ["flask", "run", "--host", "0.0.0.0"]

        # volumes: 
        #     - ./jenkins-data:/var/jenkins_home
        #     - /var/run/docker.sock:/var/run/docker.sock
