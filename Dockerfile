FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "innovation.wsgi" ]