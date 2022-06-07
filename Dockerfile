FROM python:3.10-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update && apt-get -y upgrade

RUN useradd --create-home appuser

USER appuser

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY config.py .
COPY myStreamingClient.py .

CMD [ "python", "-u", "./main.py" ]