# DBeaver

<div class="page-toc">

<!-- toc -->

</div>

## Chave GPG

```sh
wget -nv -O- https://dbeaver.io/debs/dbeaver.gpg.key | gpg --dearmor > /etc/apt/keyrings/dbeaver.gpg
```

## Repositório

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/dbeaver.gpg] https://dbeaver.io/debs/dbeaver-ce /" > /etc/apt/sources.list.d/dbeaver.list
```

## Programas

### DBeaver Community

```sh
apt install dbeaver-ce
```
