# Kafka

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://kafka.apache.org/)
- [Documentação](https://kafka.apache.org/documentation)

## Instalação

- Imagem Docker: [apache/kafka](https://hub.docker.com/r/apache/kafka), [apache/kafka-native](https://hub.docker.com/r/apache/kafka-native)

## Gerenciadores

- [UI for Apache Kafka](https://github.com/provectus/kafka-ui) ([Docker Image](https://hub.docker.com/r/provectuslabs/kafka-ui))

## Exemplos

### docker-compose

```yaml
services:
  kafka:
    image: apache/kafka:4.2.0
    command: ["/entrypoint.sh"]
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_LISTENERS: PLAINTEXT_HOST://:9092,PLAINTEXT://:29092,CONTROLLER://:9093
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT_HOST:PLAINTEXT,PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT_HOST://localhost:9092,PLAINTEXT://kafka:29092
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@localhost:9093
    volumes:
      - ./config/kafka/entrypoint.sh:/entrypoint.sh:ro
      - kafka-secrets:/etc/kafka/secrets
      - kafka-config:/mnt/shared/config
      - kafka-data:/var/lib/kafka/data
    ports:
      - 9092:9092
    expose:
      - 29092
    healthcheck:
      test: ["CMD", "/opt/kafka/bin/kafka-cluster.sh", "cluster-id", "--bootstrap-server=localhost:9092"]
      start_period: 30s
      start_interval: 5s
      interval: 1m
      timeout: 30s
      retries: 3

  kafka-ui:
    image: provectuslabs/kafka-ui:v0.7.2
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:29092
    ports:
      - 9095:8080
    depends_on:
      kafka:
        condition: service_healthy
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost:8080/actuator/health | grep -q '{\"status\":\"UP\"}'"]
      start_period: 30s
      start_interval: 5s
      interval: 1m
      timeout: 30s
      retries: 3

volumes:
  kafka-secrets:
  kafka-config:
  kafka-data:
```

`config/kafka/entrypoint.sh`:
```sh
#!/bin/sh

set -eux

if [ ! -e ~/inited ]; then
    (
        while ! /opt/kafka/bin/kafka-cluster.sh cluster-id --bootstrap-server="localhost:9092"; do
            sleep 1s
        done

        /opt/kafka/bin/kafka-topics.sh --bootstrap-server="localhost:9092" --create --topic="meu-topico"

        > ~/inited
    ) &
fi

exec /etc/kafka/docker/run
```
