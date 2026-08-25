import streamlit as st
import re
import unicodedata

st.set_page_config(page_title="BF IA", page_icon="🤖", layout="centered")

# ==========================================
# 🧠 BF IA — Cerveau V1
# ==========================================

intentions = {
    "bonjour": {
        "mots": ["bonjour", "bjr", "salut bonjour", "bonjour bf ia"],
        "reponse": "Bonjour 👋 ! Ravi de te parler. Comment puis-je t'aider ?"
    },
    "bonsoir": {
        "mots": ["bonsoir", "bsr", "bonsoir bf ia"],
        "reponse": "Bonsoir 🌙👋 ! Comment s'est passée ta journée ?"
    },
    "salut": {
        "mots": ["salut", "slt", "coucou", "hello", "hey"],
        "reponse": "Salut 👋 ! Je suis BF IA 🇧🇫. Que puis-je faire pour toi ?"
    },
    "bonne_nuit": {
        "mots": ["bonne nuit", "je vais dormir", "je vais me coucher"],
        "reponse": "Bonne nuit 🌙😴 ! Repose-toi bien."
    },
    "nom": {
        "mots": ["ton nom", "comment tu t appelles", "comment tu t appelle",
                 "qui es tu", "tu es qui"],
        "reponse": "Je m'appelle BF IA 🤖🇧🇫."
    },
    "createur": {
        "mots": ["qui t a cree", "qui a cree bf ia", "ton createur"],
        "reponse": "Je suis BF IA, un projet d'intelligence artificielle en construction. 🤖🇧🇫"
    },
    "ca_va": {
        "mots": ["ca va", "comment ca va", "tu vas bien", "comment vas tu"],
        "reponse": "Ça va très bien 🤖😊 ! Merci de demander. Et toi ?"
    },
    "merci": {
        "mots": ["merci", "merci beaucoup", "je te remercie", "thanks"],
        "reponse": "Avec plaisir ! 😊"
    },
    "aide": {
        "mots": ["aide moi", "j ai besoin d aide", "peux tu m aider"],
        "reponse": "Bien sûr 🤝 ! Explique-moi ce dont tu as besoin et je vais essayer de t'aider."
    },
    "capitale_burkina": {
        "mots": ["capitale burkina", "capitale du burkina",
                 "capitale burkina faso", "ville capitale burkina"],
        "reponse": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫"
    },
    "burkina": {
        "mots": ["burkina faso", "pays burkina", "le burkina"],
        "reponse": "Le Burkina Faso est un pays d'Afrique de l'Ouest. Sa capitale est Ouagadougou. 🇧🇫"
    },
    "ia": {
        "mots": ["c est quoi ia", "c est quoi intelligence artificielle",
                 "definition ia", "intelligence artificielle"],
        "reponse": "L'intelligence artificielle est un domaine de l'informatique qui permet à des systèmes d'effectuer certaines tâches nécessitant habituellement des capacités humaines. 🤖"
    },
    "internet": {
        "mots": ["c est quoi internet", "internet sert a quoi",
                 "a quoi sert internet", "definition internet"],
        "reponse": "Internet est un réseau mondial qui permet aux appareils de communiquer et d'échanger des informations. 🌐"
    },
    "python": {
        "mots": ["c est quoi python", "python sert a quoi",
                 "langage python", "python programmation"],
        "reponse": "Python est un langage de programmation très utilisé pour créer des logiciels, analyser des données et développer des systèmes d'intelligence artificielle. 🐍"
    },
    "application": {
        "mots": ["c est quoi une application", "application informatique",
                 "a quoi sert une application"],
        "reponse": "Une application est un programme conçu pour effectuer une ou plusieurs tâches pour l'utilisateur. 📱"
    },
    "ordinateur": {
        "mots": ["c est quoi un ordinateur", "ordinateur sert a quoi",
                 "definition ordinateur"],
        "reponse": "Un ordinateur est une machine électronique capable de traiter, stocker et transmettre des informations. 💻"
    },
    "etudes": {
        "mots": ["comment bien etudier", "comment etudier",
                 "conseil pour etudier", "mieux etudier"],
        "reponse": "Pour mieux étudier : fixe un objectif, travaille régulièrement, fais des exercices et révise progressivement. 📚"
    },
    "maths": {
        "mots": ["aide moi en maths", "mathematique", "maths", "exercice de maths"],
        "reponse": "Bien sûr 📐 ! Donne-moi ton exercice de mathématiques."
    }
}

def nettoyer_texte(texte):
    texte = texte.lower().strip()
    texte = ''.join(c for c in unicodedata.normalize("NFD", texte)
                    if unicodedata.category(c) != "Mn")
    texte = re.sub(r"[^\w\s]", " ", texte)
    return re.sub(r"\s+", " ", texte).strip()

def demander_intelligent(question):
    texte = nettoyer_texte(question)

    for intention in intentions.values():
        for mot in intention["mots"]:
            if nettoyer_texte(mot) in texte:
                return intention["reponse"]

    return ("🤔 Je ne connais pas encore la réponse à cette question. "
            "BF IA est encore en construction et continuera d'apprendre.")

# ==========================================
# 🎨 Interface Web
# ==========================================

st.markdown("""
<style>
.block-container {max-width: 800px; padding-top: 2rem;}
.bf-title {text-align:center;}
.bf-subtitle {text-align:center;color:#666;margin-bottom:20px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="bf-title"><h1>🤖 BF IA</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="bf-subtitle">Assistant intelligent 🇧🇫</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Bonjour 👋 ! Je suis BF IA. Pose-moi une question."
    }]

for message in st.session_state.messages:
    with st.chat_message(message["role"],
                         avatar="🤖" if message["role"] == "assistant" else "👤"):
        st.markdown(message["content"])

prompt = st.chat_input("Écris ton message...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    response = demander_intelligent(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response)

with st.sidebar:
    st.markdown("## 🤖 BF IA")
    st.write("Version Web V1")
    st.write(f"🧠 {len(intentions)} catégories")
    st.divider()
    st.write("🇧🇫 Projet BF IA")
    st.caption("Le cerveau sera enrichi progressivement.")
