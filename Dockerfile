FROM python:3.10.4

LABEL tech.tomy.docker.k.backend="0.6.0"
LABEL maintainer="Tomy Hsieh @tomy0000000"

WORKDIR /usr/src/k-backend
EXPOSE 8000

# Copy Application
COPY . .

# Install pip
RUN pip install --upgrade pip poetry

# Install Dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi
