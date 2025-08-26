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
