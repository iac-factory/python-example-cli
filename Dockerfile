# syntax=docker/dockerfile:1

FROM python:3.12.5-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /application

# Prevents shell access: https://docs.docker.com/go/dockerfile-user-best-practices/
RUN adduser --no-create-home --disabled-password --home "/dev/null" --gecos "" --shell "/sbin/nologin" --uid 10000 application-user

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to pyproject.toml to avoid having to copy them into
# into this layer,
RUN --mount=type=cache,target=/root/.cache/pip --mount=type=bind,source=requirements.txt,target=requirements.txt python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pip build setuptools --requirement requirements.txt

COPY . .

RUN python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org .

# Switch to the non-privileged user to run the application.
USER application-user

# ENTRYPOINT is the process that’s executed inside the container.
# --> ENTRYPOINT should be the path to the process that will be executed inside the container.
ENTRYPOINT ["python-example-cli"]

# CMD is the default set of arguments that are supplied to the ENTRYPOINT process.
# --> CMD should be the default arguments to pass to that command (if any).
CMD ["--help"]


