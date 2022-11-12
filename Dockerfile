FROM python:3.9

WORKDIR /hololingo-back

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY *.py ./
COPY ./src ./src

EXPOSE $PORT
CMD uvicorn main:app --host 0.0.0.0 --port 8000
