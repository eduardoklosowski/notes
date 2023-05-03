# RabbitMQ

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.rabbitmq.com/)
- [Documentação](https://www.rabbitmq.com/documentation.html)

## Estudo

- Simuladores:
  - [RabbitMQ Simulator](http://tryrabbitmq.com/)
  - [Try RabbitMQ](https://tryrabbitmq.github.io/)

## Instalação

### Debian

Pacote: [rabbitmq-server](https://packages.debian.org/stable/rabbitmq-server)

### Docker

Imagem: [rabbitmq](https://hub.docker.com/_/rabbitmq/)

## Config

### Virtual Hosts

Listar virtual hosts:

```sh
rabbitmqctl -q list_vhosts
```

Criar virtual host:

```sh
rabbitmqctl add_vhost <nome>
```

Remover virtual host:

```sh
rabbitmqctl delete_vhost <nome>
```

### Usuários

Listar usuários:

```sh
rabbitmqctl -q list_users
```

Criar usuários:

```sh
rabbitmqctl add_user <usuário> <senha>
```

Trocar senha do usuário:

```sh
rabbitmqctl change_password <usuário> <senha>
```

Remover usuário:

```sh
rabbitmqctl delete_user <usuário>
```

Listar permissões em um virtual host:

```sh
rabbitmqctl -q list_permissions --vhost <virtual_host>
```

Remover todas as permissões de um usuário em um virtual host:

```sh
rabbitmqctl clear_permissions --vhost <virtual_host> <usuário>
```

Atribuir permissões para um usuário (`'.*'` para todos os recursos):

```sh
rabbitmqctl set_permissions --vhost <virtual_host> <usuário> <config_perm> <write_perm> <read_perm>
```

Permitir que usuário acesso interface web:

```sh
rabbitmqctl set_user_tags <usuário> management
```

### Plugins

Mostrar plugins disponíveis e quais estão habilitados:

```sh
rabbitmq-plugins list
```

Habilitar plugin sem o serviço rodando (ideal para colocar no `Dockerfile`):

```sh
rabbitmq-plugins enable --offline <plugin> [<plugin> ...]
```

Verificar se um plugin está habilitado:

```sh
rabbitmq-plugins -q is_enabled <plugin>
```

## Health Check

[Documentação](https://www.rabbitmq.com/monitoring.html#health-checks)

Verificar se o runtime está em execução:

```sh
rabbitmq-diagnostics -q ping
```

Informações gerais do nó:

```sh
rabbitmq-diagnostics -q status
```

Verificar se o RabbitMQ está em execução:

```sh
rabbitmq-diagnostics -q check_running
```

Verificar alarmes no nó:

```sh
rabbitmq-diagnostics -q check_local_alarms
```

Verificar conectividade das portas:

```sh
rabbitmq-diagnostics -q check_port_connectivity
```

Verificar se virtual hosts estão rodando:

```sh
rabbitmq-diagnostics -q check_virtual_hosts
```

### Prometheus

URL: `http://<hostname>:15692/metrics`

## Exemplos

### docker-compose

```yml
services:
  rabbitmq:
    image: rabbitmq:3.11-management-alpine
    environment:
      RABBITMQ_DEFAULT_USER: "guest"
      RABBITMQ_DEFAULT_PASS: "guest"
      RABBITMQ_DEFAULT_VHOST: "/"
    ports:
      - 5672:5672
      - 15672:15672
    volumes:
      - rabbitmq-data:/var/lib/rabbitmq
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "-q", "check_running"]
volumes:
  rabbitmq-data:
```

### Python

Exemplo em Python: [`rabbitmq-python.tar.gz`](rabbitmq-python.tar.gz)
