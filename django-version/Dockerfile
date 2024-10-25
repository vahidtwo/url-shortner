FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libmariadb-dev gcc curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements /opt/shortner/requirements
COPY ./requirements.txt /opt/shortner/
WORKDIR /opt/shortner

RUN pip install -r requirements.txt && pip cache purge
COPY . /opt/shortner
CMD ["bash" ,"start.sh"]

