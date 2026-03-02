# Flatpak

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://docs.flatpak.org/pt-br/latest/)

## Comandos

### Aplicativos

```sh
# Lista aplicativos instalados
flatpak list --app

# Pesquisa nos repositórios remotos
flatpak search <termo>

# Instala aplicativo
flatpak install <repositorio> <id>

# Executa aplicativo
flatpak run <id>

# Remore aplicativo
flatpak uninstall <id>
```

### Manutenção

```sh
# Atualiza tudo
flatpak update

# Remove o que não é utilizado
flatpak uninstall --unused

# Lista aplicativos em execução
flatpak ps

# Entra no contêiner do aplicativo
flatpak enter <id> <executavel>
```

### Repositório Remoto

```sh
# Lista repositórios remotos configurados
flatpak remotes

# Adiciona repositório remoto
flatpak remote-add --if-not-exists <name> <url>

# Remove repositório remoto
flatpak remote-delete <name>
```

## Configuração

```sh
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```
