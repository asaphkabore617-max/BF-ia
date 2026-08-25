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

with open("BF_IA_1200_connaissances.json", "r", encoding="utf-8") as f:
    connaissances = json.load(f)

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
        "🤔 Je ne connais pas encore cette réponse. "
        "Mon créateur peut encore m'apprendre."
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

    st.rerun()import streamlit as st

st.set_page_config(
    page_title="BF IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- STYLE ----------
st.markdown("""
<style>
    /* Fond général */
    .stApp {
        background: #ffffff;
    }

    /* Barre latérale */
    section[data-testid="stSidebar"] {
        background: #f7f7f8;
        border-right: 1px solid #e5e5e5;
    }

    /* Zone principale */
    .main-title {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        margin-bottom: 40px;
    }

    /* Message utilisateur */
    .user-message {
        background: #f4f4f4;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 12px 0;
        max-width: 80%;
        margin-left: auto;
    }

    /* Message IA */
    .ai-message {
        padding: 12px 16px;
        margin: 12px 0;
        max-width: 85%;
        line-height: 1.6;
    }

    /* Logo */
    .logo {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Boutons */
    .stButton button {
        border-radius: 10px;
        border: 1px solid #ddd;
        background: white;
    }

    .stButton button:hover {
        border-color: #999;
    }

    /* Zone de saisie */
    div[data-testid="stChatInput"] {
        padding-bottom: 20px;
    }

    /* Mobile */
    @media (max-width: 700px) {
        .main-title {
            font-size: 24px;
        }

        .user-message,
        .ai-message {
            max-width: 95%;
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------- SIDEBAR ----------
with st.sidebar:

    st.markdown(
        '<div class="logo">🤖 BF IA</div>',
        unsafe_allow_html=True
    )

    if st.button("➕ Nouvelle conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("### 💬 Conversations")

    st.caption("Aucune conversation précédente")


# ---------- MÉMOIRE DES MESSAGES ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- PAGE D'ACCUEIL ----------
if len(st.session_state.messages) == 0:

    st.markdown(
        '<div class="main-title">Comment puis-je vous aider ?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Bienvenue sur BF IA 🇧🇫</div>',
        unsafe_allow_html=True
    )


# ---------- AFFICHAGE DES MESSAGES ----------
for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f'<div class="user-message">👤 {message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="ai-message">🤖 {message["content"]}</div>',
            unsafe_allow_html=True
        )


# ---------- SAISIE ----------
prompt = st.chat_input("Message BF IA...")


if prompt:

    # Message utilisateur
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # ------------------------------------------------
    # ICI TU METTRAS TON CODE QUI APPELLE TON IA
    # ------------------------------------------------

    reponse = "Je suis BF IA 🤖. Je réfléchis à ta question..."

    # Message IA
    st.session_state.messages.append({
        "role": "assistant",
        "content": reponse
    })

    st.rerun()
