import streamlit as st
from pathlib import Path
from src.core.reader import MarkdownReader
from src.ui import components

st.set_page_config(page_title="MD Viewer Pro", layout="wide")

def main():
    caminho = components.render_sidebar(Path.cwd())
    arquivos = MarkdownReader.get_md_files(caminho)
    
    if arquivos:
        escolha = components.render_file_selector(arquivos)
        conteudo = MarkdownReader.read_file(caminho, escolha)
        
        components.render_content(conteudo) 
    else:
        st.error("Caminho inválido ou sem arquivos .md")

if __name__ == "__main__":
    main()