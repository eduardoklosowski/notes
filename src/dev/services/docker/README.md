# Docker

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.docker.com/)
- [Documentação](https://docs.docker.com/)

## Exemplos de Uso

### Remover Imagem Base de Outra

Obs: Não vai apagar a imagem efetivamente, mas remover sua tag da listagem.

```sh
docker image ls --digests
docker image rm <image>@<digest>
```

### Salvar Imagem em Disco

Obs: A imagem importada terá outro hash.

```sh
docker image save image:latest -o image.tar
docker image import image.tar image:latest
```

## Ferramentas Terceiras

- [Conversor docker run para docker compose](https://www.composerize.com/)
- [Conversor docker compose para docker run](https://www.decomposerize.com/)
