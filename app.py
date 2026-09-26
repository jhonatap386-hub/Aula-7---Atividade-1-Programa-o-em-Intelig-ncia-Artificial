## Atividade 1 ##

import streamlit as st
import re

# Configuração da página
st.set_page_config(page_title="Tokenizador de Textos", layout="centered")

st.title("⚙️ Tokenizador de Mensagens")
st.write("Cole a mensagem do cliente abaixo para separar o texto em tokens (palavras) e facilitar a análise.")

# Entrada de texto
texto_bruto = st.text_area("Texto bruto:", height=150, placeholder="Digite ou cole a mensagem aqui...")

if st.button("Processar Texto"):
    if texto_bruto.strip():
        # Tokenização usando Regex (extrai sequências de caracteres alfanuméricos)
        tokens = re.findall(r'\b\w+\b', texto_bruto.lower())
        
        st.success(f"Foram encontrados {len(tokens)} tokens no texto.")
        
        # Exibe os tokens em formato de lista interativa no Streamlit
        st.write("### Lista de Tokens:")
        st.json(tokens)
    else:
        st.warning("Por favor, insira algum texto antes de processar.")