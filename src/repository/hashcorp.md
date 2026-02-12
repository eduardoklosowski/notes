# Hashcorp

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://www.hashicorp.com/pt/official-packaging-guide)

## Chave GPG

```sh
wget -nv -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /etc/apt/keyrings/hashicorp.gpg
```

## Repositório

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/hashicorp.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" > /etc/apt/sources.list.d/hashicorp.list
```

## Programas

### Terraform

```sh
apt install terraform

apt policy terraform
apt install terraform=1.9.8-1
apt-mark hold terraform

# terraform -install-autocomplete
echo "complete -C '$(which terraform)' terraform" > ~/.local/share/bash-completion/completions/terraform
```
