# Certificados TLS

<div class="page-toc">

<!-- toc -->

</div>

## Certificado Autoassinado

**Gerar chave privada:**

```sh
openssl genrsa -out privado.key 1024

openssl genpkey -algorithm ed25519 -out privado.key

openssl ecparam -list_curves
openssl ecparam -genkey -name secp256k1 -noout -out privado.key
```

**Gerar certificado:**

```sh
openssl req -x509 -new -key privado.key -out certificado.crt -subj '/CN=localhost' -days 365

openssl req -x509 -new -key privado.key -out certificado.crt -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost,IP:127.0.0.1,DNS:localhost.127.0.0.1.nip.io' -days 365
```

**Comando único:**

```sh
openssl req -x509 -newkey rsa:1024 -noenc -keyout privado.key -out certificado.crt -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost' -days 365

openssl req -x509 -newkey ed25519 -noenc -keyout privado.key -out certificado.crt -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost' -days 365
```

## Requisição de Certificado

**Gera requisição:**

```sh
openssl req -new -key privado.key -out requisicao.csr -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost'

openssl req -newkey ed25519 -noenc -keyout privado.key -out requisicao.csr -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost'
```

**Assina requisição:**

```sh
openssl x509 -req -CA ca-certificado.crt -CAkey ca-privado.key -in requisicao.csr -out certificado.crt -copy_extensions copy -days 365
```

## PKCS-12

**Gera bundle do certificado e chave:**

```sh
openssl pkcs12 -export -in certificado.crt -inkey privado.key -out combinado.pfx -passout pass:

openssl pkcs12 -export -in certificado.crt -inkey privado.key -out combinado.pfx -passout pass: -name nome-do-certificado

openssl pkcs12 -export -in certificado.crt -inkey privado.key -out combinado.pfx -passout pass:123456 -name nome-do-certificado
```

## Visualizar Informações

**Chave:**

```sh
openssl rsa -in privado.key -noout -text -check
openssl rsa -in privado.key -pubout | openssl rsa -pubin -noout -text

openssl pkey -in privado.key -noout -text -check
openssl pkey -in privado.key -pubout | openssl pkey -pubin -noout -text -check

openssl ec -in privado.key -noout -text -check
openssl ec -in privado.key -pubout | openssl ec -pubin -noout -text

openssl pkcs12 -in combinado.pfx -info
```

**Requisição de certificado:**

```sh
openssl req -in requisicao.csr -noout -text -verify
```

**Certificado:**

```sh
openssl x509 -in certificado.crt -noout -text

openssl x509 -in certificado.crt -noout -pubkey
```

**Valida cadeia de certificados:**

```sh
openssl verify -CAfile ca.crt -untrusted intermediario.crt servidor.crt
openssl verify -CAfile ca.crt -untrusted intermediario.crt ca.crt intermediario.crt folha.crt
```

**Exibe certificado de servidor HTTPS:**

```sh
get-cert() {
  # Arg1: Endereço do servidor
  # Arg2: Porta do servidor
  # Arg3: Hostname, se diferente do endereço
  echo | openssl s_client -servername "${3:-$1}" -connect "$1":"$2" | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > certificate.crt
}
```

## Autoridade Certificadora (CA)

`Makefile`:
```makefile
SERVER_HOST := server.127.0.0.1.nip.io
CLIENT_HOST := client.127.0.0.1.nip.io

.PHONY: certs clean run-server run-server-mtls run-client run-client-verify run-client-mtls

certs: ca.key ca.crt server.127.0.0.1.nip.io.key server.127.0.0.1.nip.io.crt client.127.0.0.1.nip.io.key client.127.0.0.1.nip.io.crt

ca.key:
	openssl genpkey -algorithm ed25519 -out $@

ca.crt: ca.key
	openssl req -x509 -new -key $< -out $@ -subj '/CN=Minha CA' -days 3653

%.key:
	openssl genpkey -algorithm ed25519 -out $@

%.csr: %.key
	openssl req -new -key $< -out $@ -subj '/CN=$*'

%.crt: %.csr ca.crt ca.key
	openssl x509 -req -CA ca.crt -CAkey ca.key -in $< -out $@ -copy_extensions copy -days 365

clean:
	rm -f *.key *.crt *.csr

run-server: $(SERVER_HOST).key $(SERVER_HOST).crt
	openssl s_server -port 4433 -key $(SERVER_HOST).key -cert $(SERVER_HOST).crt

run-server-mtls: $(SERVER_HOST).key $(SERVER_HOST).crt ca.crt
	openssl s_server -port 4433 -key $(SERVER_HOST).key -cert $(SERVER_HOST).crt -Verify 1 -verify_return_error -CAfile ca.crt

run-client:
	openssl s_client -connect $(SERVER_HOST)

run-client-verify: ca.crt
	openssl s_client -connect $(SERVER_HOST) -verify_return_error -CAfile ca.crt

run-client-mtls: ca.crt $(CLIENT_HOST).key $(CLIENT_HOST).crt
	openssl s_client -connect $(SERVER_HOST) -verify_return_error -CAfile ca.crt -key $(CLIENT_HOST).key -cert $(CLIENT_HOST).crt
```
