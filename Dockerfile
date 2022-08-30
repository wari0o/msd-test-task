FROM python:3.9-alpine

EXPOSE 8080

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8080