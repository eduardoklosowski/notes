# Redirecionamento de Porta

<div class="page-toc">

<!-- toc -->

</div>

## socat

O [socat](http://www.dest-unreach.org/socat/) é um programa para fazer encaminhamento de sockets. Ele pode ser utilizado para abrir uma porta local e redirecionar o tráfego para outro endereço. Exemplo:

```sh
# Porta TCP
socat -dd TCP-LISTEN:8080,fork,reuseaddr TCP:10.0.0.1:80

# Porta UDP
socat -dd UDP-LISTEN:8080,fork,reuseaddr UDP:10.0.0.1:8000

# UNIX Socket
socat -dd TCP-LISTEN:8080,fork,reuseaddr UNIX:/var/run/http.sock
```
