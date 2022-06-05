FROM python:3-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]