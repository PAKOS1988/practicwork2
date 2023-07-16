FROM python:3.10

WORKDIR /practicwork2

COPY .requirements.txt /practicwork2/requirements.txt

RUN pip3.10 install -r requirements.txt

COPY . /practicwork2

CMD ["uvicorn", "main:app", "--reload", "-host=0.0.0.0"]