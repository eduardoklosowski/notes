# Mozilla

<div class="page-toc">

<!-- toc -->

</div>

## Chave GPG

```sh
wget -nv -O- https://packages.mozilla.org/apt/repo-signing-key.gpg | gpg --dearmor -o /etc/apt/keyrings/mozilla.gpg
```

## Programas

### Firefox

- [Documentação](https://support.mozilla.org/pt-BR/kb/instale-o-firefox-no-linux#w_instale-o-pacote-deb-do-firefox-em-distribuicoes-baseadas-em-debian-recomendado)

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/mozilla.gpg] https://packages.mozilla.org/apt mozilla main" > /etc/apt/sources.list.d/mozilla.list
```

```sh
apt install firefox firefox-l10n-pt-br

update-alternatives --install /usr/bin/x-www-browser x-www-browser /usr/bin/firefox 99
```

Firefox Developer Edition:
```sh
apt install firefox-devedition firefox-devedition-l10n-pt-br

update-alternatives --install /usr/bin/x-www-browser x-www-browser /usr/bin/firefox-devedition 99
```

Não preferir pacote do repositório do Ubuntu:
```sh
cat >/etc/apt/preferences.d/firefox <<EOF
Package: firefox
Pin: origin br.archive.ubuntu.com
Pin-Priority: 50
EOF
```

#### Configuração
  - `browser.tabs.closeWindowWithLastTab`: `false`
  - `browser.tabs.insertRelatedAfterCurrent`: `false`
  - `browser.urlbar.trimURLs`: `false`

### Thunderbird

- [Documentação](https://support.mozilla.org/pt-BR/kb/instalando-o-thunderbird-no-linux#w_instale-o-pacote-deb-para-distribuicoes-baseadas-em-debian-e-ubuntu-recomendado)

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/mozilla.gpg] https://packages.mozilla.org/apt thunderbird-deb main" > /etc/apt/sources.list.d/thunderbird.list
```

```sh
apt install thunderbird thunderbird-l10n-pt-br
```
