# Amazon Web Services (AWS)

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://aws.amazon.com/pt/)
- [Documentação](https://docs.aws.amazon.com/)

**Ferramentas auxiliares:**

- [AWS Policy Generator](https://awspolicygen.s3.us-east-1.amazonaws.com/policygen.html)

## Mocks

### LocalStack

- [Site](https://www.localstack.cloud/)
- [Documentação](https://docs.localstack.cloud/)

**Verificar status:**

```sh
curl -s http://localhost:4566/_localstack/init
curl -s http://localhost:4566/_localstack/init/ready
```

**Imagem Docker:**

- [Docker Hub](https://hub.docker.com/r/localstack/localstack)

```yaml
services:
  aws:
    image: localstack/localstack:4.1.1
    restart: unless-stopped
    volumes:
      - aws-data:/var/lib/localstack
      - /var/run/docker.sock:/var/run/docker.sock
      - ./init.sh:/etc/localstack/init/ready.d/init.sh:ro  # Script para criar recursos
    ports:
      - 4566:4566
      - 4510-4559:4510-4559
volumes:
  aws-data:
```
