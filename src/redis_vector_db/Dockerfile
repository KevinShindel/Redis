FROM redis/redis-stack-server:latest
LABEL maintainer="Kevin Shindel"
EXPOSE 6379 6380

# Add a user for redis
RUN adduser --system --group --no-create-home redis && \
    chsh -s /bin/bash redis

RUN mkdir -p /data/redis
RUN chown redis:redis /data/redis
RUN chmod 770 /data/redis

RUN mkdir -p /var/log/redis
RUN mkdir /etc/redis
RUN touch /var/log/redis/redis.log
RUN chmod 770 /var/log/redis/

COPY redis.conf /etc/redis/redis.conf
CMD [ "redis-server", "/etc/redis/redis.conf"]