# Sockets

<div class="page-toc">

<!-- toc -->

</div>

## UNIX

### Servidor UNIX

```sh
socat -dd stdio unix-listen:app.sock,fork
```

### Cliente UNIX

```sh
socat -dd stdio unix-connect:app.sock
```

## UDP

### Servidor UDP

```sh
nc -vulp 8000

socat -dd stdio udp-listen:8000,fork,reuseaddr
```

### Cliente UDP

```sh
nc -vu localhost 8000

socat -dd stdio udp-connect:localhost:8000
```

## TCP

### Servidor TCP

```sh
nc -vlp 8000

socat -dd stdio tcp-listen:8000,fork,reuseaddr
```

### Cliente TCP

```sh
nc -v localhost 8000

socat -dd stdio tcp-connect:localhost:8000
```
