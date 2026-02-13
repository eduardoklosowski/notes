# Amazon Elastic Container Registry

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação](https://docs.aws.amazon.com/ecr/)
- [ECR Public Gallery](https://gallery.ecr.aws/)

```sh
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

docker tag <image> <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<image>
```
