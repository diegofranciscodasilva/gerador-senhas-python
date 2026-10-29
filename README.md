# Gerador de senhas

Aplicativo de terminal em Python para gerar senhas aleatórias com pelo menos 16 caracteres.

## Requisitos

- Python 3.6 ou superior
- Nenhuma dependência externa

## Como executar

No terminal, acesse a pasta do projeto e execute:

```bash
python gerador_senha.py
```

No Windows, também é possível usar o iniciador `py`:

```powershell
py gerador_senha.py
```

Informe o tamanho desejado, que deve ser de pelo menos 16 caracteres. O programa gera a senha usando letras maiúsculas e minúsculas, números e pontuação, e a exibe no terminal.

## Segurança

A geração usa o módulo `secrets` da biblioteca padrão do Python, apropriado para valores aleatórios usados em senhas. Cada caractere é escolhido do conjunto combinado; não há garantia de que toda senha contenha ao menos um caractere de cada categoria.

## 👨‍💻 Autor

### Diego Francisco da Silva

Desenvolvedor Front-End em formação e estudante de Engenharia de Software.

- **[Site Empresa](https://diegofranciscodasilva.github.io/dev-software-web/)**: dev.software.web Site Empresa
- **[LinkedIn](https://www.linkedin.com/in/diego-francisco-da-silva/)**: diego-francisco-da-silva
- **[GitHub](https://github.com/diegofranciscodasilva)**: diegofranciscodasilva
- **[Instagram](https://www.instagram.com/diego_francisco_da_silva/)**: @diego_francisco_da_silva
- **[Instagram](https://www.instagram.com/dev.software.web/)**: @dev.software.web

---

Feito com ❤️ por Diego.
