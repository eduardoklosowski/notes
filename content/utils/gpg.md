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

## Exportar/Importar uma Chave

```sh
# Exporta Chave Pública
gpg --armor --export <id-chave>

# Exporta Chave Privada
gpg --armor --export-secret-keys <id-chave>

# Importa Chave
gpg --import <arquivo-chave>
gpg --edit-key <id-chave>
```

## Deleta uma Chave

```sh
# Deleta Chave Pública
gpg --delete-keys <id-chave>

# Deleta Chave Privada
gpg --delete-secret-keys <id-chave>
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

## Servidor de Chaves

- [keys.openpgp.org](https://keys.openpgp.org/)
- [OpenPGP keyserver](https://keyserver.ubuntu.com/)
- [Debian Public Key Server](https://keyring.debian.org/)

Servidor pode ser definido com o parâmetro `--keyserver hkps://keyserver.ubuntu.com:443`.

```sh
# Baixar chave
gpg --recv-keys <id-chave>

# Enviar chave
gpg --send-keys <id-chave>

# Procura por chave no servidor
gpg --search-keys <pesquisa>

# Atualiza chaves locais
gpg --refresh-keys
```
