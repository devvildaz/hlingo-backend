FROM python

WORKDIR /hololingo-back

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

EXPOSE $PORT
CMD uvicorn src.main:app --host 0.0.0.0 --port $PORT
