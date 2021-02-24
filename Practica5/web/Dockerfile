FROM python:3
ENV PYTHONUNBUFFERED 1

# Creating working directory inside container
RUN mkdir /web
COPY . /web
COPY requirements.txt /web
WORKDIR /web
RUN pip3 install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:$PORT