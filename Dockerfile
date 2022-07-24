FROM python:3.9
ENV HOME=/home/app/web
RUN mkdir -p $HOME
WORKDIR $HOME
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . $HOME
EXPOSE 8000
WORKDIR $HOME/flight_tracking_application
CMD python manage.py runserver