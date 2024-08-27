# Gerador de senhas

Um aplicativo para gerar senhas de acordo com as escolhas do usuário.

## Descrição

Este projeto é um gerador de senhas que tem as seguintes funcionalidades:
- **Definir o tamanho da senha**
- **Optar por letras maiúsculas**
- **Optar por letras minúsculas**
- **Optar por números**
- **Optar por símbolos**
- **Gerar uma nova senha**
- **Encerrar o programa**


## Requisitos

- Python 3.6 ou superior
- Cx_Freeze

## Instalação

1. **Clone este repositório:**

    ```bash
    git clone https://github.com/cadumrod/password_generator
    cd password_generator
    ```

2. **Crie e ative um ambiente virtual:**

    No Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    No macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Construa o executável com `cx_Freeze`**:

    ```bash
    python setup.py build
    ```

## Uso

1. Após a construção, o executável estará disponível no diretório `build`. Para executar o aplicativo, navegue até o diretório de saída (por exemplo, `build/exe.win-amd64-3.12` no Windows) e execute o arquivo gerado:

    No Windows:
    ```bash
    cd build/exe.win-amd64-3.12
    app.exe
    ```

    No macOS/Linux:
    ```bash
    cd build/exe.macosx-10.6-intel-3.12
    ./app
    ```


## Estrutura do Projeto

- `app.py`: Arquivo principal do aplicativo.
- `python.ico`: Ícone usado no aplicativo.
- `setup.py`: Script de instalação e configuração do projeto.
- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Arquivo de requisitos com as dependências do projeto.
- `LICENSE`: Licença MIT.


## Autor

**Carlos Rodrigues**

- [GitHub](https://github.com/cadumrod)
- [E-mail](mailto:carlosrod.dev@gmail.com)

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.