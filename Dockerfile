FROM python:3.7-alpine as build

COPY requirements.txt requirements.txt
RUN python -m venv /venv
RUN apk add --update gcc python3-dev musl-dev
RUN /venv/bin/pip install -r requirements.txt
RUN /venv/bin/pip install gunicorn

FROM python:3.7-alpine

COPY --from=build /venv /venv

RUN apk --no-cache add libpq

RUN adduser -D nhltv


WORKDIR /home/nhltv

COPY alembic alembic
COPY app app
COPY run.py config.py boot.sh alembic.ini ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

RUN chown -R nhltv:nhltv ./
USER nhltv

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
