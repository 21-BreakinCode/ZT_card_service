ARG VARIANT=3.9-bullseye
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

COPY . /app

WORKDIR /app

## real-time logging and better debugging ##
ENV PYTHONUNBUFFERED 1

RUN pip install -r ./src/requirements.txt

EXPOSE  80

CMD ["uvicorn", "--app-dir", "src", "main:app", "--host", "0.0.0.0"]
