# Sockets

<div class="page-toc">

<!-- toc -->

</div>

Ferramentas:
- [netcat](http://www.stearns.org/nc/)
- [socat](http://www.dest-unreach.org/socat/)
- [microsocks](https://github.com/rofl0r/microsocks)

## Testar Conexão

### TCP

#### Servidor TCP

```sh
nc -vlp 8000
```

```sh
socat -dd stdio tcp-listen:8000,fork,reuseaddr
```

#### Cliente TCP

```sh
nc -v localhost 8000
```

```sh
socat -dd stdio tcp-connect:localhost:8000
```

### UDP

#### Servidor UDP

```sh
nc -vulp 8000
```

```sh
socat -dd stdio udp-listen:8000,fork,reuseaddr
```

#### Cliente UDP

```sh
nc -vu localhost 8000
```

```sh
socat -dd stdio udp-connect:localhost:8000
```

### UNIX

#### Servidor UNIX

```sh
socat -dd stdio unix-listen:app.sock,fork
```

#### Cliente UNIX

```sh
socat -dd stdio unix-connect:app.sock
```

## Redirecionamento de Porta

### TCP

```sh
socat -dd TCP-LISTEN:8080,fork,reuseaddr TCP:10.0.0.1:80
```

### UDP

```sh
socat -dd UDP-LISTEN:8080,fork,reuseaddr UDP:10.0.0.1:8000
```

### UNIX

```sh
socat -dd TCP-LISTEN:8080,fork,reuseaddr UNIX:/var/run/http.sock
```
