# XML - eXtensible Markup Language

<div class="page-toc">

<!-- toc -->

</div>

## Formatar

- **Pacote:** [libxml2-utils](https://packages.debian.org/sid/libxml2-utils)

```sh
xmllint --format arquivo.xml
```

## Validar Schema

```xml
<?xml version="1.0" encoding="UTF-8"?>
<base
  xmlns="http://localhost/namespace"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://localhost/namespace http://localhost/namespace/schema.xsd">
</base>
```

```sh
xmllint --schema schema.xsd --noout arquivo.xml
```

## Assinatura

- **Pacote:** [xmlsec1](https://packages.debian.org/sid/xmlsec1)

`exemplo.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<MeuXml>
  <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:SignedInfo>
      <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <ds:Reference URI="#key-info-id">
        <ds:Transforms>
          <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
        </ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue/>
      </ds:Reference>
      <ds:Reference URI="">
        <ds:Transforms>
          <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
          <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
        </ds:Transforms>
        <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <ds:DigestValue/>
      </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue/>
    <ds:KeyInfo Id="key-info-id">
      <ds:X509Data>
        <ds:X509IssuerSerial>
          <ds:X509IssuerName>CN=Minha CA</ds:X509IssuerName>
          <ds:X509SerialNumber>1234567890</ds:X509SerialNumber>
        </ds:X509IssuerSerial>
      </ds:X509Data>
    </ds:KeyInfo>
  </ds:Signature>
  <Dados>
    <Nome>Exemplo</Nome>
  </Dados>
</MeuXml>
```

```sh
# Assinar XML
xmlsec1 --sign --output output.xml --privkey-pem cert.key,cert.crt input.xml

# Validar Assinatura do XML
xmlsec1 --verify --pubkey-cert-pem cert.crt arquivo.xml
```
