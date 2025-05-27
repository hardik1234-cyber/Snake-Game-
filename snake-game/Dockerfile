FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app

ENV DISPLAY=:0

EXPOSE 8000

CMD ["python", "snakegame.py"]
