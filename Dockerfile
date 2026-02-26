# FROM      - Image(Snapshot, vår startpunkt)
# WORKDIR   - Working directory ("/app") - A new folder within docker, called app
# COPY      - Extract a duplicate copy of our app (app snapshot)
# EXPOSE    - Includes a port that OS uses
# CMD       - Commands to be run on start up.
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv pip install --system -r pyproject.toml
COPY . .
CMD ["uvicorn", "10_lecture_kafka_rabbitmq.lecture_10_app:app", "--host", "0.0.0.0", "--port", "8000"]