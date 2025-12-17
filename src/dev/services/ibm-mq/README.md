# IBM MQ

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.ibm.com/br-pt/products/mq)
- [Documentação](https://www.ibm.com/docs/pt-br/ibm-mq)

## Instalação

### Docker

Imagem: [ibm-messaging](https://icr.io/v2/ibm-messaging/mq/tags/list), [ibm-messaging](https://github.com/ibm-messaging/mq-container/releases) (versões antigas)

## Config

Acessar interface de MQSC:
```sh
runmqsc
```

## Gerenciador de Filas

Mostrar informações:
```mqsc
DISPLAY QMGR
```

Alterar atributos:
```mqsc
ALTER QMGR DESCR('Meu servidor de teste')
```

## Fila

Criar fila local:
```mqsc
DEFINE QLOCAL(QUEUE.LOCAL) +
    DESCR('Minha fila local') +
    REPLACE
```

## Exemplos

- Acesso Interface web: `https://localhost:9443/`

### docker-compose

```yaml
services:
  mq:
    image: icr.io/ibm-messaging/mq:9.4.4.0-r2
    environment:
      LICENSE: "accept"
      MQ_QMGR_NAME: "QMBCB"
      MQ_ADMIN_USER: "admin"
      MQ_ADMIN_PASSWORD: "passw0rd"
      MQ_APP_USER: "app"
      MQ_APP_PASSWORD: "passw0rd"
    volumes:
      - mq-data:/mnt/mqm
    ports:
      - "1414:1414"
      - "9443:9443"
volumes:
  mq-data:
```
