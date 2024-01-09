FROM python:3.9.6-slim as base
RUN apt-get update \
    && apt-get install vim -y

# DEPENDENCIAS PYTHON
FROM base as builder

COPY requirements.txt /requirements.txt

RUN pip install --target="/install" -r /requirements.txt

FROM base as default 
WORKDIR /app


RUN mkdir /logs
COPY --from=builder /install /usr/local 
COPY app /app

RUN ["chmod", "+x", "/app/run_app.sh"]

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONWARNINGS ignore
ENV PYTHONPATH=/usr/local
ENV DEBUG=true
ENV GUNICORN_CMD_ARGS="--capture-output --access-logfile=- --log-level=debug --error-logfile=- --workers=4 --worker-class=sync"

WORKDIR /app

ENV DEBUG=false

CMD [ "/app/run_app.sh" ]