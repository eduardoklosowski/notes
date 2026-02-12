# HTTP

<div class="page-toc">

<!-- toc -->

</div>

## Proxy HTTP

### Enviar Requisições HTTP via Proxy

```sh
# Configurações de Sistema
export HTTP_PROXY='http://127.0.0.1:8080'
export HTTPS_PROXY='http://127.0.0.1:8080'
export ALL_PROXY='socks5://127.0.0.1:9050'  # Resolve DNS localmente
export ALL_PROXY='socks5h://127.0.0.1:9050'  # Resolve DNS no servidor

# cURL
curl -x http://proxy:8080 http://server

# HTTPie
http --proxy http:http://proxy:8080 http://server
http --proxy all:http://proxy:8080 http://server
```

## HTTPS

#### Validação de Certificado HTTPS

Sem validar CA:
```sh
# cURL
curl -k https://duckduckgo.com/

# HTTPie
http --verify=no https://duckduckgo.com/
```

Informando certificado da CA:
```sh
# cURL
curl --cacert cert.pem https://duckduckgo.com/

# HTTPie
http --verify=cert.pem https://duckduckgo.com/
```

### Proxy HTTPS

O [mitmproxy](https://mitmproxy.org/) pode ser utilizado como servidor proxy para visualizar as requisições HTTPS feitas, estando o cliente no mesmo dispositivo ou não. Ele pode ser executado através do docker:

```sh
# Versão TUI
docker run --rm -it -v "$(pwd)/cert:/home/mitmproxy/.mitmproxy" -p 8080:8080 mitmproxy/mitmproxy

# Versão WEB
docker run --rm -it -v "$(pwd)/cert:/home/mitmproxy/.mitmproxy" -p 8080:8080 -p 127.0.0.1:8081:8081 mitmproxy/mitmproxy mitmweb --web-host 0.0.0.0
```

Ao subir o serviço, será criado automaticamente um certificado de CA em `cert/mitmproxy-ca-cert.pem` (se não existir). Esse certificado deve ser configurado como uma CA confiável no cliente, além de configurar o proxy HTTP na porta `8080`.

A versão TUI mostrará as requisições no terminal, enquanto a versão WEB pode ser acessada na porta [`8081`](http://127.0.0.1:8081/).

### mTLS

#### Certificados

Gerar certificados:

```sh
# Servidor
openssl req -x509 -newkey ed25519 -noenc -keyout server.key -out server.crt -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost' -days 365

# Cliente
openssl req -x509 -newkey ed25519 -noenc -keyout client.key -out client.crt -subj '/CN=client' -days 365
```

#### Servidor

Executar servidor de exemplo com OpenSSL:

```sh
openssl s_server -port 4433 -www -cert server.crt -key server.key -CAfile client.crt -Verify 1 -verify_return_error
```

#### Cliente

Realizar requisições:

```sh
# cURL
curl -v --cacert server.crt --cert client.crt --key client.key https://localhost:4433/

# HTTPie
http -v --cert=client.crt --cert-key=client.key --verify=server.crt https://localhost:4433/
```
