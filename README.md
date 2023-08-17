<div align="center">
  <img src="https://github.com/EfySecurity/Coding-Tool/blob/main/icons8-base-64.gif" alt="Project Logo">
</div>

# Security Tools - Termux Script

Este é um projeto de script para operações de encode, decode e personalização desenvolvido para uso em segurança da informação. Ele permite a codificação e decodificação de dados utilizando a biblioteca base64, além de aplicar uma operação personalizada aos dados.

## Funcionalidades

- Codificação de Dados: Codifica dados de entrada utilizando a base64.
- Decodificação de Dados: Decodifica dados codificados previamente.
- Operação Personalizada: Aplica uma operação personalizada aos dados, por exemplo, substituindo vogais por números.

## Pré-requisitos

Certifique-se de ter o Python instalado no Termux.

## Como Usar


1. Clone este repositório para o seu ambiente Termux.

```bash
git clone https://github.com/EfySecurity/Coding-Tool
```

2. Abra o terminal e navegue até o diretório do projeto.

```bash
cd Coding-Tool
```

3. Execute o script `coding-tool.py` utilizando o comando.

```bash
python coding-tool.py
```

4. Siga as instruções do menu para realizar as operações desejadas.

## Exemplos

### Codificação de Dados

```plaintext
Escolha uma opção:
1. Encode
2. Decode
3. Operação Personalizada
4. Sair

Opção: 1

Digite os dados a serem codificados: Hello, world!
Dados codificados: SGVsbG8sIHdvcmxkIQ==
```

### Decodificação de Dados

```plaintext
Escolha uma opção:
1. Encode
2. Decode
3. Operação Personalizada
4. Sair

Opção: 2

Digite os dados codificados: SGVsbG8sIHdvcmxkIQ==
Dados decodificados: Hello, world!
```

### Operação Personalizada

```plaintext
Escolha uma opção:
1. Encode
2. Decode
3. Operação Personalizada
4. Sair

Opção: 3

Digite os dados para a operação personalizada: Secure password
Resultado da operação personalizada: S3cur3 p4ssw0rd

```

Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Crie um fork deste repositório, faça suas alterações e envie um pull request.

## Autor

Nome: Efy Security
Email: efy.security@proton.me

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
