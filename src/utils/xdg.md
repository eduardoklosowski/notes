# freedesktop.org

<div class="page-toc">

<!-- toc -->

</div>

## Aplicação

- [Especificação](https://specifications.freedesktop.org/desktop-entry/latest/)
- [Wiki do Arch](https://wiki.archlinux.org/title/Desktop_entries)

Diretórios:
  - `/usr/share/applications`
  - `~/.local/share/applications`

### Exemplo

`~/.local/share/applications/foobar.desktop`:
```ini
#!/usr/bin/env xdg-open

[Desktop Entry]
Version=1.0
Type=Application
Name=Foobar
Comment=Comentário do programa
GenericName=Nome genérico
Icon=foobar
Exec=foobar %F
Terminal=false
StartupNotify=true
Categories=
MimeType=
```

### Comandos

```sh
# Validar arquivo .desktop
desktop-file-validate foobar.desktop

# Adiciona arquivo .desktop
desktop-file-install foobar.desktop

# Atualiza database com os arquivos
update-desktop-database ~/.local/share/applications
```

## MIME Type

- [Especificação](https://specifications.freedesktop.org/shared-mime-info/latest/)
- [XDG MIME Applications na Wiki do Arch](https://wiki.archlinux.org/title/XDG_MIME_Applications)

Diretórios:
  - `/usr/share/mime`
  - `~/.local/share/mime`

### Exemplo

`~/.local/share/mime/packages/application-x-foobar.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-foobar">
    <comment>foo file</comment>
    <icon name="application-x-foobar"/>
    <glob-deleteall/>
    <glob pattern="*.foo"/>
  </mime-type>
</mime-info>
```

### Comandos

```sh
# Atualiza datebase com os arquivos
update-mime-database ~/.local/share/mime
```
