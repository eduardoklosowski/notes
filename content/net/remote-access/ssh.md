# SSH

<div class="page-toc">

<!-- toc -->

</div>

## Fechar acesso quando cai a conexão

As vezes quando a conexão é perdida, o terminal fica travado. Para encerrar o acesso SSH nestes casos basta digitar:

```txt
~.
```

## Manter e compartilhar sessão

O [tmux](https://github.com/tmux/tmux/wiki) pode ser usado em conjunto com o ssh para manter a sessão caso a conexão seja perdida, ou compartilhar a tela com outros usuários.

Uma forma simples de fazer isso é instalar o tmux no servidor (`apt install tmux`, por exemplo), e configurar o alias `ssht` no seu computador, que pode ser feito no arquivo `~/.bash_aliases`:

```sh
ssht() {
  ssh -t "$@" "tmux new -A -s 0"
}
```

Para o autocomplete funcionar, assim como ocorre no comando `ssh`, é necessário configurá-lo em `~/.local/share/bash-completion/completions/ssht`:

```sh
source /usr/share/bash-completion/completions/ssh
complete -F _ssh ssht
```

Após reiniciar o shell será possível conectar no servidor usando `ssht <endereço>`, exemplo `ssht localhost`. E caso a conexão seja perdida, ou usando o comando `Ctrl + b, d` (se não foi alterado na configuração do tmux), basta usar o mesmo comando para reconectar no servidor e voltar a sessão que estava aberta.

## Acesso Através de Outro Sevidor

```
Host <host-desejado>
  ProxyJump [<user-proxy>@]<host-proxy>[:<port-proxy>]
  ProxyCommand ssh <host-proxy> -W %h:%p
  ProxyCommand ssh <host-proxy> nc %h %p
```
