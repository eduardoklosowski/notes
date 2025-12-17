# HTTPS com mTLS

<div class="page-toc">

<!-- toc -->

</div>

## Certificados

Gerar certificados:

```sh
# Servidor
openssl req -x509 -newkey ed25519 -noenc -keyout server.key -out server.crt -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost' -days 365

# Cliente
openssl req -x509 -newkey ed25519 -noenc -keyout client.key -out client.crt -subj '/CN=client' -days 365
```

## Servidor

Executar servidor de exemplo com OpenSSL:

```sh
openssl s_server -port 4433 -www -cert server.crt -key server.key -CAfile client.crt -Verify 1 -verify_return_error
```

## Cliente

Realizar requisições:

```sh
# cURL
curl -v --cacert server.crt --cert client.crt --key client.key https://localhost:4433/

# HTTPie
http -v --cert=client.crt --cert-key=client.key --verify=server.crt https://localhost:4433/
```
