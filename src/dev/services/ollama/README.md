# Ollama

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://ollama.com/)
- [Documentação](https://docs.ollama.com/)

## Instalação

### Completa no Sistema

```sh
cd /usr/local
wget -O- https://ollama.com/download/ollama-linux-amd64.tar.zst | tar --zstd -xf -

# bash-completion
wget -O /etc/bash_completion.d/ollama https://github.com/ehrlz/ollama-bash-completion-plugin/raw/refs/heads/main/plugin.sh
```

### Simplificada para o Usuário

```sh
cd ~/.local/bin
wget -O- https://ollama.com/download/ollama-linux-amd64.tar.zst | tar --zstd -xf - bin/ollama --strip-components=1

# bash-completion
wget -O ~/.local/share/bash-completion/completions/ollama https://github.com/ehrlz/ollama-bash-completion-plugin/raw/refs/heads/main/plugin.sh
```

## Execução

Inicia serviço:

```sh
ollama serve
```

Baixa LLM:

```sh
ollama pull <name>:<tag>
```

Executa LLM no terminal iterativo:

```sh
ollama run <name>:<tag>
```

## LLM

- [gemma4](https://ollama.com/library/gemma4)
- [qwen3.5](https://ollama.com/library/qwen3.5)
- [granite4](https://ollama.com/library/granite4)

## Open WebUI

- [Documentação](https://docs.openwebui.com/)

Executa ollama ouvindo via rede:

```sh
OLLAMA_HOST=172.17.0.1:11434 ollama serve
```

Executa Open WebUI:

```sh
docker run -it --rm -p 3000:8080 --add-host=host.docker.internal:host-gateway ghcr.io/open-webui/open-webui:main-slim
```

### docker-compose

```yml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main-slim
    volumes:
      - open-webui:/app/backend/data
    ports:
      - 3000:8080
    extra_hosts:
      - host.docker.internal:host-gateway
volumes:
  open-webui:
```
