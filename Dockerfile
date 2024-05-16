FROM python:latest

WORKDIR /app

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD flask --app main.py run --debug -p 5000 --host 0.0.0.0