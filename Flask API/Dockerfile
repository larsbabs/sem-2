FROM python:3.9.1
ADD . /checksum-api
WORKDIR /checksum-api
RUN pip install -r requirements.txt
CMD [ "python3.9", "./api.py" ]