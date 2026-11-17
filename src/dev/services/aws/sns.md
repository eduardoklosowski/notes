# Amazon Simple Notification Service (SNS)

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://docs.aws.amazon.com/sns/)

## Comandos

### Tópico

#### Lista Tópicos

```sh
aws sns list-topics
```

#### Cria Tópico

```sh
aws sns create-topic --name <nome-topico>
```

#### Mostra Atributos do Tópico

```sh
aws sns get-topic-attributes --topic-arn <arn-topico>
```

#### Apaga Tópico

```sh
aws sns delete-topic --topic-arn <arn-topico>
```

### Assinatura

#### Assina Tópico

```sh
aws sns subscribe --topic-arn <arn-topico> --protocol sqs --notification-endpoint <arn-fila>

# Mensagem em raw
aws sns subscribe --topic-arn <arn-topico> --protocol sqs --notification-endpoint <arn-fila> --attributes RawMessageDelivery=true

## Filtra por header
aws sns subscribe --topic-arn <arn-topico> --protocol sqs --notification-endpoint <arn-fila> --attributes '{"RawMessageDelivery": "true", "FilterPolicyScope": "MessageAttributes", "FilterPolicy": "{\"key\": [\"value\"]}"}'

# Filtra por body
aws sns subscribe --topic-arn <arn-topico> --protocol sqs --notification-endpoint <arn-fila> --attributes '{"RawMessageDelivery": "true", "FilterPolicyScope": "MessageBody", "FilterPolicy": "{\"key\": [\"value\"]}"}'
```

#### Lista Assinaturas do Tópico

```sh
aws sns list-subscriptions-by-topic --topic-arn <arn-topico>
```

#### Detalhes de Assinatura do Tópico

```sh
aws sns get-subscription-attributes --subscription-arn <arn-assinatura>
```

#### Remove Assinatura do Tópico

```sh
aws sns unsubscribe --subscription-arn <arn-assinatura>
```

### Envia Mensagem

```sh
aws sns publish --topic-arn <arn-topico> --message <mensagem>

# Mensagens com Atributos
aws sns publish --topic-arn <arn-topico> --message <mensagem> --message-attributes <atributos>
# Atributos -> 'Chave1={DataType=String,StringValue=Valor1},Chave2={DataType=String,StringValue=Valor2}'
```
