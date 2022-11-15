FROM python:3.9

WORKDIR /module

COPY ./requirements.txt /module/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /module/requirements.txt

COPY ./api /module/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
