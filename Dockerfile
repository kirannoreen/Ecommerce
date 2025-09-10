FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install required system dependencies (added pkg-config + default-libmysqlclient-dev)
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     build-essential \
     libpq-dev \
     default-libmysqlclient-dev \
     pkg-config \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/logs

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
