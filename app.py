import streamlit as st
import json
import unicodedata
import re

st.set_page_config(
    page_title="BF IA",
    page_icon="🤖"
)

# ====================================
# Charger les connaissances
# ====================================

# Charger les connaissances générales
with open("BF_IA_1200_connaissances.json", "r", encoding="utf-8") as f:
    connaissances = json.load(f)

# Charger les connaissances de mathématiques
with open("BF_IA_Maths.json", "r", encoding="utf-8") as f:
    connaissances_maths = json.load(f)

# Regrouper toutes les connaissances
connaissances.update(connaissances_maths)

# ====================================
# Fonction nettoyage
# ====================================

def nettoyer(texte):
    texte = texte.lower()

    texte = ''.join(
        c for c in unicodedata.normalize('NFD', texte)
        if unicodedata.category(c) != 'Mn'
    )

    texte = re.sub(r'[^\w\s]', ' ', texte)
    texte = re.sub(r'\s+', ' ', texte)

    return texte.strip()

# ====================================
# Recherche intelligente
# ====================================

def repondre(question):

    q = nettoyer(question)

    for cle, reponse in connaissances.items():

        if nettoyer(cle) in q:
            return reponse

    return (
        "🤔 Je ne connais pas encore la réponse a cette question. "
        "Mon créateur ASAPH continue encore à m'apprendre et serai bientôt opérationnel."
    )

# ====================================
# Interface
# ====================================

st.title("🤖 BF IA")
st.write("Assistant intelligent du Burkina Faso 🇧🇫")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Pose une question...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    reponse = repondre(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reponse
    })

    st.rerun()
