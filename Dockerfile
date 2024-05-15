FROM python:latest

WORKDIR /root

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]