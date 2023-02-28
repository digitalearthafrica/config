FROM alpine:latest

RUN apk --no-cache add bash curl jq git

WORKDIR /opt/dea-geoserver

COPY ./scripts ./scripts
COPY docker-entrypoint.sh .
RUN chmod 755 /opt/dea-geoserver/docker-entrypoint.sh

ENTRYPOINT ["/opt/dea-geoserver/docker-entrypoint.sh"]
CMD [ "/opt/dea-geoserver/scripts/geoserver-docker.sh" ]