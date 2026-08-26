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
# ==========================================
# 🧠 RECHERCHE INTELLIGENTE DE BF IA
# ==========================================

def répondre(question):
    q = nettoyer(question)

    # 1️⃣ Recherche exacte
    for clé, réponse in connaissances.items():
        clé_nettoyee = nettoyer(str(clé))

        if clé_nettoyee in q:
            return réponse

    # 2️⃣ Recherche par mots importants
    mots_question = set(q.split())

    meilleure_reponse = None
    meilleur_score = 0

    for clé, réponse in connaissances.items():
        clé_nettoyee = nettoyer(str(clé))
        mots_clé = set(clé_nettoyee.split())

        if not mots_clé:
            continue

        # Nombre de mots communs
        communs = mots_question.intersection(mots_clé)
        score = len(communs)

        # On garde la meilleure correspondance
        if score > meilleur_score:
            meilleur_score = score
            meilleure_reponse = réponse

    # On accepte la réponse seulement si suffisamment de mots correspondent
    if meilleure_reponse is not None and meilleur_score >= 1:
        return meilleure_reponse

    # 3️⃣ Si BF IA ne trouve rien
    return (
        "🤔 Je ne connais pas encore cette information.\n\n"
        "Mon créateur ASAPH continue d'améliorer BF IA 🧠🇧🇫 et je serai bientôt opérationnel"
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
