import streamlit as st
import streamlit_mermaid as st_mermaid
import re

def render_sidebar(default_path):
    st.sidebar.title("📁 Navegador")
    path = st.sidebar.text_input("Caminho da pasta:", value=default_path)
    return path

def render_file_selector(files):
    indice_idx = 0
    for i, f in enumerate(files):
        if f.name == "README.md" or f.name == "INDICE.md":
            indice_idx = i
            break
    
    return st.sidebar.radio("Documentos:", files, index=indice_idx, format_func=lambda x: x.name)

def _render_mermaid_block(chart_code, index):
    with st.expander(f"📊 Visualizar Fluxo #{index}"):
        st_mermaid.st_mermaid(chart_code)

def render_content(content):
    parts = re.split(r'(```mermaid\n[\s\S]*?\n```)', content)
    
    mermaid_count = 0
    for part in parts:
        if part.startswith('```mermaid'):
            mermaid_count += 1
            chart_code = part.replace('```mermaid\n', '').replace('```', '').strip()
            _render_mermaid_block(chart_code, mermaid_count)
        else:
            st.markdown(part, unsafe_allow_html=True)