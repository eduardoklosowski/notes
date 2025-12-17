# OpenTelemetry

<div class="page-toc">

<!-- toc -->

</div>

- [Site do OpenTelemetry](https://opentelemetry.io/pt/)
- [Documentação geral](https://opentelemetry.io/pt/docs/)
- Notas por linguagem:
  - [Python](../../lang/python/opentelemetry.md)

## Imagens

### Grafana - All in One

- [Documentação](https://github.com/grafana/docker-otel-lgtm)
- [Docker Hub](https://hub.docker.com/r/grafana/otel-lgtm)

**Informações de Acesso:**
- Endereço: <http://localhost:3000/>
- Usuário: `admin`
- Senha: `admin`

Na inicialização cria arquivo `/tmp/ready` quando pronto.

**Exemplo de docker compose:**
```yaml
services:
  olgtm:
    image: grafana/otel-lgtm:0.13.0
    volumes:
      - olgtm-data:/data
    ports:
      - 3000:3000  # Grafana
      - 4317:4317  # OpenTelemetry GRPC
      - 4318:4318  # OpenTelemetry HTTP
    healthcheck:
      test: [ "CMD-SHELL", "curl -f http://localhost:3000/api/health || exit 1" ]
      start_period: 20s
      start_interval: 5s
      interval: 1m
      timeout: 5s
      retries: 3
volumes:
  olgtm-data:
```
