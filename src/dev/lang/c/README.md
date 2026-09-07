# C

<div class="page-toc">

<!-- toc -->

</div>

- [Documentação da Biblioteca](https://cplusplus.com/reference/clibrary/)

## Bibliotecas

### Bibliotecas Compartilhadas

Argumentos do GCC:
- `-I` diretório com os arquivos headers
- `-L` diretório com as libs `lib*.so`
- `-l` biblioteca a ser utilizada

Variável de ambiente para locais onde procurar bibliotecas: `LD_LIBRARY_PATH`

Lista bibliotecas compartilhas presentes no sistema:
```sh
ldconfig -p
```

Lista símbolos dinâmicos presentes na bibliote compartilhada:
```sh
nm -D libexemplo.so
```

## Exemplos

- [Usando biblioteca estática e dinâmica](example-lib.tar.gz)
