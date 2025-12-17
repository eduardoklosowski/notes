# Microsoft

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://learn.microsoft.com/en-us/linux/packages)

## Chave GPG

```sh
wget -nv -O- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/keyrings/microsoft.gpg
```

## Programas

### Visual Studio Code

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/code/ stable main" > /etc/apt/sources.list.d/code.list
```

```sh
apt install code
```

### Edge

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/edge/ stable main" > /etc/apt/sources.list.d/edge.list
```

```sh
apt install microsoft-edge-stable
```
