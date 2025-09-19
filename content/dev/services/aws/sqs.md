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

### Mostra Atributos da Fila

```sh
aws sqs get-queue-attributes --queue-url <url-fila> --attribute-names All
```

### Apaga Fila

```sh
aws sqs delete-queue --queue-url <url-fila>
```

### Envia Mensagem

```sh
aws sqs send-message --queue-url <url-fila> --message-body <mensagem>

# Mensagens com Atributos
aws sqs send-message --queue-url <url-fila> --message-body <mensagem> --message-attributes <atributos>
# Atributos -> 'Chave1={DataType=String,StringValue=Valor1},Chave2={DataType=String,StringValue=Valor2}'
```

### Receber Mensagem

```sh
aws sqs receive-message --queue-url <url-fila> --max-number-of-messages 10 --wait-time-seconds 10 --visibility-timeout 30

# Mensagens com Atributos
aws sqs receive-message --queue-url <url-fila> --max-number-of-messages 10 --wait-time-seconds 10 --visibility-timeout 30 --message-system-attribute-names All --message-attribute-names All

# Aumentar Tempo de Processamento
aws sqs change-message-visibility --queue-url <url-fila> --receipt-handle <codigo-da-mensagem> --visibility-timeout 120

# Apaga Mensagem Recebida
aws sqs delete-message --queue-url <url-fila> --receipt-handle <codigo-da-mensagem>
```
