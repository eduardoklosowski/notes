# Amazon Web Services (AWS)

<div class="page-toc">

<!-- toc -->

</div>

- [Site](https://aws.amazon.com/pt/)
- [Documentação](https://docs.aws.amazon.com/)
- [Referência de Configuração](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html)

**Ferramentas auxiliares:**

- [AWS Policy Generator](https://awspolicygen.s3.us-east-1.amazonaws.com/policygen.html)

## Cliente CLI

- [Documentação CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/)
- [Manual de referência da CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)
- [Listagem das versões](https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst)

### Instalação

```sh
curl -o awscliv2.zip https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.24.12.zip
unzip -q awscliv2.zip
sudo ./aws/install
rm -rf awscliv2.zip aws
```

#### Completion

**Bash:**

```sh
echo "complete -C \"$(which aws_completer)\" aws" > ~/.local/share/bash-completion/completions/aws
```

### Configuração

#### Chave Simples

**Cria configuração de forma iterativa:**
```sh
aws configure
aws configure --profile=user1
AWS_PROFILE=localstack aws configure
```

**Arquivos de configuração:**

`~/.aws/config`:
```ini
[default]
region=us-west-1
#output=json

[profile user1]
region=us-east-1
#output=text

[profile localstack]
region=us-east-1
#output=table
endpoint_url=http://localhost:4566
```

`~/.aws/credentials`:
```ini
[default]
aws_access_key_id=ASIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
aws_session_token = IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE

[user1]
aws_access_key_id=ASIAI44QH8DHBEXAMPLE
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
aws_session_token = fcZib3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE

[localstack]
aws_access_key_id = test
aws_secret_access_key = test
```

#### Integrado ao SSO

**Cria configuração de forma iterativa:**
```sh
aws configure sso
aws configure sso --profile=user1
```

**Arquivos de configuração:**

`~/.aws/config`:
```ini
[profile user1]
sso_session = my-sso
sso_account_id = 123456789012
sso_role_name = my-role
region = us-east-1
#output = json

[sso-session my-sso]
sso_region = us-east-1
sso_start_url = https://sso.mycompany.com/start
sso_registration_scopes = sso:account:access
```

**Atualiza credenciais/Login:**
```sh
aws sso login --profile=user1
AWS_PROFILE=user1 aws sso login
```

### Testa Configuração

```sh
aws sts get-caller-identity
aws sts get-caller-identity --profile=user1
AWS_PROFILE=localstack aws sts get-caller-identity
AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test AWS_SESSION_TOKEN=test AWS_DEFAULT_REGION=us-east-1 AWS_ENDPOINT_URL=http://localhost:4566 aws sts get-caller-identity
```

## Mocks

### LocalStack

- [Site](https://www.localstack.cloud/)
- [Documentação](https://docs.localstack.cloud/)

**Verificar status:**

```sh
curl -s http://localhost:4566/_localstack/init
curl -s http://localhost:4566/_localstack/init/ready
```

**Imagem Docker:**

- [Docker Hub](https://hub.docker.com/r/localstack/localstack)

```yaml
services:
  aws:
    image: localstack/localstack:4.1.1
    restart: unless-stopped
    volumes:
      - aws-data:/var/lib/localstack
      - /var/run/docker.sock:/var/run/docker.sock
      - ./init.sh:/etc/localstack/init/ready.d/init.sh:ro  # Script para criar recursos
    ports:
      - 4566:4566
      - 4510-4559:4510-4559
volumes:
  aws-data:
```
