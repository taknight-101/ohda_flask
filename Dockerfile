FROM python:3.9

WORKDIR /ohda

COPY requirements.txt ./
COPY . .
# RUN apt-get install libmysqlclient-dev
# RUN apt-get install python-dev
# RUN pip install mysql-python
RUN pip install  -r requirements.txt
# RUN export DB_URL=//db/flask
# RUN pip install --no-cache-dir -r requirements.txt

CMD python app.py