# Markdown Preview

Projeto para visualização de arquivos markdown em uma interface gráfica simples.

## Requisitos

- Python 3.12
- Streamlit
- Markdown

## Instalação

Recomenda-se a criação de um ambiente virtual para a execução do projeto.

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Se não quiser criar um ambiente virtual, pode instalar os requisitos globalmente:

```sh
pip install -r requirements.txt
```

## Uso

```sh
streamlit run main.py
```

## Erros conhecidos

- [] os links internos do markdown estão abrindo uma nova guia invez de ir para o link
- [x] Trocar o impot os pelo impoort PATH por questão de segurança


## TODO

- [] Adicionar um botão pra navegar entre os arquivos
- [] Botão pra trancar o caminho digitado (pra não apagar acidentalmente)
- [x] renderizar mermaid
- [] Busca global da informaçãona pasta entre os arquivos


