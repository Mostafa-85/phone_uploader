FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=phone_Project.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
