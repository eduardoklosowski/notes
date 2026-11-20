# AWS Key Management Service (KMS)

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://docs.aws.amazon.com/kms/)

## Comandos

### Chave

#### Lista Chaves

```sh
aws kms list-keys
```

#### Detalhes da Chave

```sh
aws kms describe-key --key-id <key>
```

#### Ativa/Desativa Chave

```sh
aws kms enable-key --key-id <key-id>
aws kms disable-key --key-id <key-id>
```

#### Apaga Chave

```sh
aws kms schedule-key-deletion --key-id <key-id> --pending-window-in-days 7
```

### Alias

#### Lista Alias

```sh
aws kms list-aliases
```

#### Cria Alias

```sh
aws kms create-alias --alias-name <nome> --target-key-id <key-id>
```

#### Apaga Alias

```sh
aws kms delete-alias --alias-name <nome>
```

### Chave Assimétrica

#### Cria Chave Assimétrica

```sh
aws kms create-key --description <descricao> --key-usage <ENCRYPT_DECRYPT|SIGN_VERIFY> --key-spec RSA_2048
```

#### Importa Chave Assimétrica

```sh
KEY_ID="$(aws kms create-key \
  --description="Chave de exemplo" \
  --key-usage="SIGN_VERIFY" \
  --key-spec="RSA_2048" \
  --origin="EXTERNAL" \
  --output="text" --query="KeyMetadata.KeyId"
)"
PARAMS="$(aws kms get-parameters-for-import \
  --key-id="$KEY_ID" \
  --wrapping-algorithm="RSA_AES_KEY_WRAP_SHA_256" \
  --wrapping-key-spec="RSA_4096" \
  --output="text" --query="[ImportToken,PublicKey]"
)"
AES_KEY="$(openssl rand 32)"
aws kms import-key-material \
  --key-id="$KEY_ID" \
  --import-token=fileb://<(echo "$PARAMS" | cut -f1 | base64 --decode) \
  --encrypted-key-material=fileb://<(
    openssl pkeyutl -encrypt \
      -in <(echo -n "$AES_KEY") \
      -inkey <(echo "$PARAMS" | cut -f2 | base64 --decode) \
      -keyform DER -pubin \
      -pkeyopt rsa_padding_mode:oaep \
      -pkeyopt rsa_oaep_md:sha256 \
      -pkeyopt rsa_mgf1_md:sha256
    openssl enc -id-aes256-wrap-pad \
      -K "$(echo -n "$AES_KEY" | od -An -v -tx1 | tr -d ' \n')" \
      -iv A65959A6 \
      -in <(openssl pkcs8 -topk8 -nocrypt -outform der -in data/bcb-sign/client.key)
  ) \
  --expiration-model="KEY_MATERIAL_DOES_NOT_EXPIRE" \
  --output="off"
```

#### Recupera Chave Pública

```sh
aws kms get-public-key --key-id <key> --output text --query PublicKey | base64 -d | openssl rsa -pubin
```
