import streamlit as st
import os
from src.core.reader import MarkdownReader
from src.ui import components

st.set_page_config(page_title="MD Viewer Pro", layout="wide")

def main():
    caminho = components.render_sidebar(os.getcwd())
    
    arquivos = MarkdownReader.get_md_files(caminho)
    
    if arquivos:
        escolha = components.render_file_selector(arquivos)
        
        conteudo = MarkdownReader.read_file(caminho, escolha)
        
        st.markdown(conteudo, unsafe_allow_html=True)
    else:
        st.error("Nenhum arquivo .md ou caminho inválido.")

if __name__ == "__main__":
    main()