FROM continuumio/anaconda3


WORKDIR /app

COPY ./* .

CMD [ "python", "./app.py" ]
