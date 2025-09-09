# Amazon Simple Queue Service (SQS)

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://docs.aws.amazon.com/sqs/)

## Comandos

### Lista Filas

```sh
aws sqs list-queues
```

### Criar Fila

```sh
aws sqs create-queue --queue-name <nome-fila>
```

### Recupera URL da Fila

```sh
aws sqs get-queue-url --queue-name <nome-fila> --output text --query QueueUrl
```

### Apaga Fila

```sh
aws sqs delete-queue --queue-url <url-fila>
```
