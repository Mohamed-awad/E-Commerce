FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /django_e-commerce

WORKDIR /django_e-commerce

ADD . /django_e-commerce

RUN pip3 install -r requirements.txt

RUN python3 manage.py migrate

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]

