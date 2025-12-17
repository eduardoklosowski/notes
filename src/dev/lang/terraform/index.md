# Terraform

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://www.terraform.io/)
- [Documentação](https://developer.hashicorp.com/terraform)
- [Módulos](https://registry.terraform.io/)

## Instalação

### Repositório APT

```sh
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /etc/apt/keyrings.d/hashicorp-package.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings.d/hashicorp-package.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" > /etc/apt/sources.list.d/hashicorp.list
apt update && apt policy terraform
apt install terraform=1.9.8-1
apt-mark hold terraform
```

### Completion

**Bash:**

```sh
# terraform -install-autocomplete
echo "complete -C '$(which terraform)' terraform" > /etc/bash_completion.d/terraform
```

## Exemplos

### Cloud

- [AWS](exemplo-aws.tar.gz)
