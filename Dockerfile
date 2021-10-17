
FROM python:3.10.0


WORKDIR /weather-API


COPY ./requirements.txt /code/requirements.txt


RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt


COPY ./src /weather-API/src


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
