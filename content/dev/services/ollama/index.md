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
wget -O- https://ollama.com/download/ollama-linux-amd64.tgz | tar -xzf -

# bash-completion
wget -O /etc/bash_completion.d/ollama https://github.com/ehrlz/ollama-bash-completion-plugin/raw/refs/heads/main/plugin.sh
```

### Simplificada para o Usuário

```sh
cd ~/.local/bin
wget -O- https://ollama.com/download/ollama-linux-amd64.tgz | tar -xzf - bin/ollama --strip-components=1

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
ollama run <name>:<tag>
```

Executa LLM no terminal iterativo:

```sh
ollama run <name>:<tag>
```

## LLM

- [gemma3](https://ollama.com/library/gemma3)
- [qwen3](https://ollama.com/library/qwen3)
