# DNS

<div class="page-toc">

<!-- toc -->

</div>

## Testar Consulta

### Requisição Direta

**`host`:**
- Pacote Debian: [`bind9-host`](https://packages.debian.org/stable/bind9-host)

```sh
host [-v] [-4|-6] [-T|-U] [-t <type>] [-p <port>] <name> [<server>]
```

**`dig`:**
- Pacote Debian: [`bind9-dnsutils`](https://packages.debian.org/stable/bind9-dnsutils)

```sh
dig [@<server>] [-4|-6] [-t <type>] [-p <port>] <name> [<type>]
```

### DNS over HTTPS (DoH)

```sh
curl -H "accept: application/dns-json" "https://<server>/dns-query?name=<domain-name>"
```
