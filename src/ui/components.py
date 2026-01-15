import streamlit as st

def render_sidebar(default_path):
    st.sidebar.title("📁 Navegador")
    path = st.sidebar.text_input("Caminho da pasta:", value=default_path)
    return path

def render_file_selector(files):
    indice_idx = 0
    if "INDICE.md" in files:
        indice_idx = files.index("INDICE.md")
    
    return st.sidebar.radio("Documentos:", files, index=indice_idx)