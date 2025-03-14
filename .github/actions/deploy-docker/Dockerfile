FROM python:3

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY update_and_create_tag.py /update_and_create_tag.py

CMD ["python", "/update_and_create_tag.py"]
