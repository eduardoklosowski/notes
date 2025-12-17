# Kubernetes

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://kubernetes.io/pt-br/docs/tasks/tools/install-kubectl-linux/#instale-usando-o-gerenciador-de-pacotes-nativo)

## Chave GPG

```sh
wget -nv -O- "https://pkgs.k8s.io/core:/stable:/$(wget -q -O- https://dl.k8s.io/release/stable.txt | sed -r 's/^(v[0-9]+\.[0-9]+).*/\1/')/deb/Release.key" | gpg --dearmor > /etc/apt/keyrings/kubernetes.gpg
```

## Repositório

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/kubernetes.gpg] https://pkgs.k8s.io/core:/stable:/$(wget -q -O- https://dl.k8s.io/release/stable.txt | sed -r 's/^(v[0-9]+\.[0-9]+).*/\1/')/deb/ /" > /etc/apt/sources.list.d/kubernetes.list
```

## Programas

### kubectl

```sh
apt install kubectl

echo '. <(kubectl completion bash)' > ~/.local/share/bash-completion/completions/kubectl
```
