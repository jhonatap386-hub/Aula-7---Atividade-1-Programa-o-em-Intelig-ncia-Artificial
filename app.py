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


## Atividade 2 ##

from collections import Counter
import re

texto = "o sistema travou, o erro é constante e o app é ruim"
# Reutilizando a lógica da Atividade 1
tokens = re.findall(r'\b\w+\b', texto.lower())

# Conta a frequência
frequencia = Counter(tokens)
print(frequencia) 
# Resultado: Counter({'o': 3, 'é': 2, 'sistema': 1, 'travou': 1, 'erro': 1, 'constante': 1, 'app': 1, 'ruim': 1})


## Atividade 3 ##

palavras_negativas = {"ruim", "péssimo", "erro", "horrível", "lento"}
mensagem = "estou com um erro no meu aplicativo"

tokens_mensagem = set(re.findall(r'\b\w+\b', mensagem.lower()))

# Verifica se existe intersecção entre a mensagem e a lista negra
alerta_prioridade = bool(palavras_negativas.intersection(tokens_mensagem))

if alerta_prioridade:
    print("🚨 ALERTA: Mensagem negativa detectada. Priorizar atendimento.")

## Atividade 4 ##

stopwords = {"de", "a", "o", "para", "e", "com", "um", "uma"}
texto = "o cliente enviou uma mensagem para a empresa"

tokens = re.findall(r'\b\w+\b', texto.lower())
tokens_limpos = [palavra for palavra in tokens if palavra not in stopwords]

print(tokens_limpos)
# Resultado: ['cliente', 'enviou', 'mensagem', 'empresa']

## Atividade 5 ##

positivas = {"bom", "ótimo", "excelente", "gostei", "rápido"}
negativas = {"ruim", "péssimo", "erro", "demora", "lento"}

comentario = "o atendimento foi rápido, mas o produto é ruim e tem erro"
tokens = re.findall(r'\b\w+\b', comentario.lower())

score = 0
for palavra in tokens:
    if palavra in positivas:
        score += 1
    elif palavra in negativas:
        score -= 1

if score > 0:
    print("Sentimento: Positivo 🟢")
elif score < 0:
    print("Sentimento: Negativo 🔴")
else:
    print("Sentimento: Neutro ⚪")

## Atividade 6 ##

mensagem = "preciso cancelar minha assinatura devido a um erro de pagamento"
tokens = set(re.findall(r'\b\w+\b', mensagem.lower()))

if {"cancelar", "cancelamento"}.intersection(tokens):
    setor = "Retenção"
elif {"pagamento", "fatura", "cartão"}.intersection(tokens):
    setor = "Financeiro"
elif {"erro", "bug", "falha"}.intersection(tokens):
    setor = "Suporte Técnico"
else:
    setor = "Atendimento Geral"

print(f"Direcionando cliente para o setor: {setor}")

## Atividade 7 ##

from collections import Counter

reclamacao = "o app travou, tentei abrir o app e travou de novo, erro péssimo"
stopwords = {"o", "e", "de"}

tokens = re.findall(r'\b\w+\b', reclamacao.lower())
tokens_uteis = [p for p in tokens if p not in stopwords]

top_3_problemas = Counter(tokens_uteis).most_common(3)
print("Principais termos da reclamação:", top_3_problemas)
# Resultado: [('app', 2), ('travou', 2), ('tentei', 1)]

## Atividade 8 ##

def classificar_mensagem(texto):
    tokens = set(re.findall(r'\b\w+\b', texto.lower()))
    
    tags_financeiras = {"boleto", "pix", "pagamento", "cobrança", "reembolso"}
    tags_tecnicas = {"senha", "login", "erro", "sistema", "carrega"}
    
    if tags_financeiras.intersection(tokens):
        return "FINANCEIRO"
    if tags_tecnicas.intersection(tokens):
        return "SUPORTE_TECNICO"
    
    return "OUTROS"

print(classificar_mensagem("meu boleto venceu ontem")) # Retorna: FINANCEIRO

## Atividade 9 ##

import re

texto_sujo = "Olá!!! Tudo bem? O sistema (finalmente) funcionou: 100% incrível."

# Substitui o que não é alfanumérico ou espaço por vazio
texto_limpo = re.sub(r'[^\w\s]', '', texto_sujo)
texto_normalizado = texto_limpo.lower()

print(texto_normalizado)
# Resultado: olá tudo bem o sistema finalmente funcionou 100 incrível

## Atividade 10 ##

import re

def analisar_avaliacao(texto_bruto):
    # 1. Limpeza e Normalização
    texto_limpo = re.sub(r'[^\w\s]', '', texto_bruto).lower()
    
    # 2. Tokenização
    tokens = texto_limpo.split()
    
    # 3. Dicionários de Sentimento
    positivas = {"amei", "recomendo", "ótimo", "bom", "rápido", "funciona"}
    negativas = {"odeio", "ruim", "péssimo", "quebrado", "defeito", "nunca"}
    
    # 4. Análise Condicional
    score = sum(1 for p in tokens if p in positivas) - sum(1 for p in tokens if p in negativas)
    
    if score > 0:
        return "🟢 Cliente Satisfeito"
    elif score < 0:
        return "🔴 Cliente Insatisfeito"
    else:
        return "⚪ Neutro ou Misto"

# Teste
avaliacao = "Comprei o produto e amei! Funciona super bem, recomendo muito."
print(analisar_avaliacao(avaliacao))
