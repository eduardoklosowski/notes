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
