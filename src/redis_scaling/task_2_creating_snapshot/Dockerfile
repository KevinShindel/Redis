FROM redis:6.2.5
LABEL authors="Tymur_Hilfatullin"
LABEL version="1.0.0"
LABEL description="Redis 6.2.5"
ENV IMAGE_NAME="redis-server"
ENV TAG="6.2.5"

RUN apt-get update && apt-get install -y \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY ./redis.conf /usr/local/etc/redis/
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
