FROM python:3.8-slim-buster





WORKDIR /myapp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY requirements.txt ./


RUN pip install -r requirements.txt

COPY ./ ./





#ADD user   see link
RUN useradd -u 123 my-user
USER my-user



CMD ["python", "./battlefield.py"]