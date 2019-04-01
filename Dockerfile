FROM alpine

RUN apk update && \
    apk add \
        bash \
        curl \
        python3 \
        py3-pip && \
    pip3 install pipenv && \
    curl -Lo /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it && \
    adduser -S conroy && \
    mkdir /app && \
    chown conroy /app

WORKDIR /app

USER conroy

COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY . .

CMD ["pipenv", "run", "python", "main.py"]