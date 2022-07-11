FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY netapp /netapp

RUN python3 netapp/manage.py makemigrations
RUN python3 netapp/manage.py migrate