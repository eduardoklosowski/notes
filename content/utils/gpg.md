# GPG

<div class="page-toc">

<!-- toc -->

</div>

## Gerar Chave

```sh
gpg --full-generate-key
```

## Listar Chaves

```sh
# Chaves Privadas
gpg -K
gpg --list-secret-keys --keyid-format LONG

# Chaves Públicas
gpg -k
gpg --list-keys --keyid-format LONG
```

## Criptografia e Assinatura

```sh
# Assinar em Arquivo Separado
gpg -sbu <id-chave> <arquivo>
gpg -sbu <id-chave> -a -o <assinatura> <arquivo>
gpg --sign --detach-sign --local-user <id-chave> --armor --output <assinatura> <arquivo>

# Verifica Assinatura
gpg --verify <assinatura> <arquivo>

# Criptografa e Assina
gpg -seu <id-chave-origem> -r <id-chave-destino> -a -o <criptografado> <arquivo>
gpg --sign --encrypt --local-user <id-chave-origem> --recipient <id-chave-destino> --armor --output <criptografado> <arquivo>

# Descriptografa validando assinatura
gpg -d <criptografado>
gpg --decrypt --output <arquivo> <criptografado>
```
