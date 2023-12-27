# Proxy

<div class="page-toc">

<!-- toc -->

</div>

## Servidor

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

## Cliente

### Requisições HTTPS via Proxy

```sh
# Define proxy
export HTTP_PROXY=http://127.0.0.1:8080
export HTTPS_PROXY=http://127.0.0.1:8080

# cURL sem validar CA
curl -v -k https://duckduckgo.com/

# cURL informando certificado da CA
curl -v --cacert mitmproxy-ca-cert.pem https://duckduckgo.com/

# HTTPie sem validar CA
http -v --verify=no https://duckduckgo.com/

# HTTPie informando certificado da CA
http -v --verify=mitmproxy-ca-cert.pem https://duckduckgo.com/
```
