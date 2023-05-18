FROM python:3.9.6
ADD . /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]