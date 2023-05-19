# Python

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.python.org/)
- [Documentação](https://docs.python.org/pt-br/3/)

## Instalar Aplicação

### pipx

[Site](https://pypa.github.io/pipx/)

O pipx permite instalar aplicações Python (pacotes) em VirtualEnv, disponibilizando seus executáveis para serem utilizados fora dele.

#### Instalação

Escolha uma das opções:

**Gerenciador de pacotes:**

```sh
apt install pipx
```

**Manual:**

```sh
python -m venv ~/.local/python-apps
~/.local/python-apps/bin/pip install pipx
ln -s ~/.local/python-apps/bin/pipx ~/.local/bin/pipx
```

##### Completion

**Bash:**

**Gerenciador de pacotes:**

```sh
echo 'eval "$(register-python-argcomplete3 pipx)"' > ~/.local/share/bash-completion/completions/pipx
```

**Manual:**

```sh
echo 'eval "$($HOME/.local/python-apps/bin/register-python-argcomplete pipx)"' > ~/.local/share/bash-completion/completions/pipx
```

#### Comandos

Listar aplicações instaladas:

```sh
pipx list --include-injected
```

Instalar aplicação:

```sh
pipx install <pacote>
```

Instalar aplicação no mesmo VirtualEnv de outra:

```sh
pipx inject <virtualenv> <pacote>
```

Atualizar todas as aplicações:

```sh
pipx upgrade-all --include-injected
```

## Ambiente de Desenvolvimento

### pyenv

[Site](https://github.com/pyenv/pyenv)

O pyenv permite instalar e gerenciar várias versões diferentes do Python.

#### Instalação

```sh
git clone https://github.com/pyenv/pyenv.git ~/.pyenv --single-branch --depth=1
ln -s ~/.pyenv/bin/pyenv ~/.local/bin/pyenv

# Dependências para compilar o Python
apt install make gcc zlib1g-dev libssl-dev

# Dependências opcionais para algumas libs da biblioteca padrão do Python
apt install libbz2-dev libncurses-dev libffi-dev libreadline-dev libsqlite3-dev liblzma-dev

# [Opcional] Melhora a performance
cd ~/.pyenv
src/configure
make -C src
```

##### Completion

**bash:**

```sh
ln -s ~/.pyenv/completions/pyenv.bash ~/.local/share/bash-completion/completions/pyenv
```

##### Atualização

Copiar script [`update-pyenv`](update-pyenv) para `~/.local/bin`.

#### Instalar Versões do Python

Listar versões disponíveis:

```sh
pyenv install -l
```

Instalar versão desejada:

```sh
pyenv install <versão>
```

Executáveis do Python podem ser encontrados em `~/.pyenv/versions/<versão>/bin/python`.

### Poetry

[Site](https://python-poetry.org/)

#### Instalação

```sh
pipx install poetry

# Plugins
pipx inject poetry <pacote-do-plugin>
```

##### Completion

**bash:**

```sh
echo 'eval "$(poetry completions bash)"' > ~/.local/share/bash-completion/completions/poetry
```

#### Plugins

- [Dynamic versioning plugin for Poetry](https://github.com/mtkennerly/poetry-dynamic-versioning) (pacote: `poetry-dynamic-versioning[plugin]`)

#### Configuração

Listar parâmetros:

```sh
poetry config --list
```

Recupera valor de um parâmetro:

```sh
poetry config <parâmetro>
```

#### VirtualEnvs

Listar VirtualEnvs do projeto:

```sh
poetry env list
```

Informações sobre o VirtualEnv atual:

```sh
poetry env info
```

Criar novo VirtualEnv com uma versão específica do Python:

```sh
poetry env use ~/.pyenv/versions/<versão>/bin/python
```

Remover VirtualEnv:

```sh
poetry env remove <nome do venv>
```

Rodar comando dentro do VirtualEnv:

```sh
poetry run <comando>
```

Abrir shell dentro do VirtualEnv:

```sh
poetry shell
```
