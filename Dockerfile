# base image
FROM python:3-alpine

# install dependencies
RUN apk update \
    && apk add build-base \
    && apk add install gcc \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2-binary \
    && apk del build-deps

# on defini le dossier par défaut du container et d'ailleur c'est pour ca que dans le requirements.txt je n'ai pas besoin de faire app/requirements.txt
# enfaite dans le containers on a le dossier racine et dedans on trouve le dossier app car c'est ce qu'on a copier plus bas
# c'est bizarre mais il faut définir workdir avant copy alors que le dossier app est créer après copy!!
WORKDIR /app

#copier mon dossier app en local dans le dossier racine du container
COPY app .


# depuis le dossier racine dans le container run le fichier requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000



CMD ["flask", "run", "--host", "0.0.0.0"]

