FROM cgr.dev/chainguard/python:latest AS runtime

COPY app /app

WORKDIR /app

# REPLACE: run command here
ENTRYPOINT ["python", "main.py"]
