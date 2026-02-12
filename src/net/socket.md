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

## Proxy SOCKS

### MicroSocks

- **Pacote:** [microsocks](https://packages.debian.org/stable/microsocks)

```sh
# Configuração padrão
microsocks

# Ourir na rede
microsocks -i 0.0.0.0 -p 1080

# Autentica acesso
microsocks -u username -P password

# Define IP de saída
microsocks -b 10.0.0.5
```

### gost - GO Simple Tunnel

- [Releases](https://github.com/ginuerzh/gost/releases/)

```sh
wget -O- https://github.com/ginuerzh/gost/releases/download/v2.12.0/gost_2.12.0_linux_amd64.tar.gz | tar -xzf - gost

# Serviço local
./gost -L=socks5://127.0.0.1:1080

# Ouvir na rede
./gost -L=socks5://:1080

# Autentica acesso
./gost -L=socks5://user:senha@:1080
```

### Clientes

```sh
curl -x socks5h://server:1080 https://ifconfig.me
```
