# Slack

<div class="page-toc">

<!-- toc -->

</div>

## Chave GPG

```sh
wget -nv -O- https://packagecloud.io/slacktechnologies/slack/gpgkey | gpg --dearmor -o /etc/apt/keyrings/slack.gpg
```

## Repositório

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/slack.gpg] https://packagecloud.io/slacktechnologies/slack/debian jessie main" > /etc/apt/sources.list.d/slack.list
```

## Programas

### Slack Desktop

```sh
apt install slack-desktop
```
