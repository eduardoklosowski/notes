# Make

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.gnu.org/software/make/)

## Comandos

```makefile
# Alvo padrão
.DEFAULT_GOAL := target

# Não verifica se o alvo está atualizado no disco
.PHONY: target
```

## Receitas

### help - Lista Comandos

```makefile
help:  ## Lista comandos
	@awk 'BEGIN {FS = ":.*## "} /^[0-9A-Za-z-_.\$$/].*:.*## / {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
```
