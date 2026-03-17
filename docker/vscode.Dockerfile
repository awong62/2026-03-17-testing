FROM python:3.12-slim

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates git \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN pip install --no-cache-dir pandas matplotlib pytest

RUN useradd -m -s /bin/bash coder \
    && mkdir -p /project \
    && chown -R coder:coder /project

USER coder
WORKDIR /project

EXPOSE 8080

CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "/project"]