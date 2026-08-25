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
        "🤔 Je ne connais pas encore la réponse à cette question. "
        "Mon créateur Asaph m'apprend encore et je serai prêt dans les jours à venir."
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
{
  "capitale du Burkina Faso": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Peux-tu me dire capitale du Burkina Faso ?": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Je veux savoir capitale du Burkina Faso.": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Explique-moi capitale du Burkina Faso.": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Dis-moi capitale du Burkina Faso.": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Quelle est la réponse concernant capitale du Burkina Faso ?": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Tu sais capitale du Burkina Faso ?": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Donne-moi une information sur capitale du Burkina Faso.": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "J’aimerais connaître capitale du Burkina Faso.": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "Réponds à la question : capitale du Burkina Faso.": "La capitale du Burkina Faso est Ouagadougou. 🇧🇫",
  "monnaie du Burkina Faso": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Peux-tu me dire monnaie du Burkina Faso ?": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Je veux savoir monnaie du Burkina Faso.": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Explique-moi monnaie du Burkina Faso.": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Dis-moi monnaie du Burkina Faso.": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Quelle est la réponse concernant monnaie du Burkina Faso ?": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Tu sais monnaie du Burkina Faso ?": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Donne-moi une information sur monnaie du Burkina Faso.": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "J’aimerais connaître monnaie du Burkina Faso.": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "Réponds à la question : monnaie du Burkina Faso.": "La monnaie utilisée au Burkina Faso est le franc CFA BCEAO (XOF).",
  "langue officielle du Burkina Faso": "La langue officielle du Burkina Faso est le français.",
  "Peux-tu me dire langue officielle du Burkina Faso ?": "La langue officielle du Burkina Faso est le français.",
  "Je veux savoir langue officielle du Burkina Faso.": "La langue officielle du Burkina Faso est le français.",
  "Explique-moi langue officielle du Burkina Faso.": "La langue officielle du Burkina Faso est le français.",
  "Dis-moi langue officielle du Burkina Faso.": "La langue officielle du Burkina Faso est le français.",
  "Quelle est la réponse concernant langue officielle du Burkina Faso ?": "La langue officielle du Burkina Faso est le français.",
  "Tu sais langue officielle du Burkina Faso ?": "La langue officielle du Burkina Faso est le français.",
  "Donne-moi une information sur langue officielle du Burkina Faso.": "La langue officielle du Burkina Faso est le français.",
  "J’aimerais connaître langue officielle du Burkina Faso.": "La langue officielle du Burkina Faso est le français.",
  "Réponds à la question : langue officielle du Burkina Faso.": "La langue officielle du Burkina Faso est le français.",
  "région du Burkina Faso": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Peux-tu me dire région du Burkina Faso ?": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Je veux savoir région du Burkina Faso.": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Explique-moi région du Burkina Faso.": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Dis-moi région du Burkina Faso.": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Quelle est la réponse concernant région du Burkina Faso ?": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Tu sais région du Burkina Faso ?": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Donne-moi une information sur région du Burkina Faso.": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "J’aimerais connaître région du Burkina Faso.": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "Réponds à la question : région du Burkina Faso.": "Le Burkina Faso se trouve en Afrique de l’Ouest.",
  "habitants du Burkina Faso": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Peux-tu me dire habitants du Burkina Faso ?": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Je veux savoir habitants du Burkina Faso.": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Explique-moi habitants du Burkina Faso.": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Dis-moi habitants du Burkina Faso.": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Quelle est la réponse concernant habitants du Burkina Faso ?": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Tu sais habitants du Burkina Faso ?": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Donne-moi une information sur habitants du Burkina Faso.": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "J’aimerais connaître habitants du Burkina Faso.": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "Réponds à la question : habitants du Burkina Faso.": "Les habitants du Burkina Faso sont appelés les Burkinabè.",
  "capitale du Ghana": "La capitale du Ghana est Accra.",
  "Peux-tu me dire capitale du Ghana ?": "La capitale du Ghana est Accra.",
  "Je veux savoir capitale du Ghana.": "La capitale du Ghana est Accra.",
  "Explique-moi capitale du Ghana.": "La capitale du Ghana est Accra.",
  "Dis-moi capitale du Ghana.": "La capitale du Ghana est Accra.",
  "Quelle est la réponse concernant capitale du Ghana ?": "La capitale du Ghana est Accra.",
  "Tu sais capitale du Ghana ?": "La capitale du Ghana est Accra.",
  "Donne-moi une information sur capitale du Ghana.": "La capitale du Ghana est Accra.",
  "J’aimerais connaître capitale du Ghana.": "La capitale du Ghana est Accra.",
  "Réponds à la question : capitale du Ghana.": "La capitale du Ghana est Accra.",
  "capitale du Mali": "La capitale du Mali est Bamako.",
  "Peux-tu me dire capitale du Mali ?": "La capitale du Mali est Bamako.",
  "Je veux savoir capitale du Mali.": "La capitale du Mali est Bamako.",
  "Explique-moi capitale du Mali.": "La capitale du Mali est Bamako.",
  "Dis-moi capitale du Mali.": "La capitale du Mali est Bamako.",
  "Quelle est la réponse concernant capitale du Mali ?": "La capitale du Mali est Bamako.",
  "Tu sais capitale du Mali ?": "La capitale du Mali est Bamako.",
  "Donne-moi une information sur capitale du Mali.": "La capitale du Mali est Bamako.",
  "J’aimerais connaître capitale du Mali.": "La capitale du Mali est Bamako.",
  "Réponds à la question : capitale du Mali.": "La capitale du Mali est Bamako.",
  "capitale du Niger": "La capitale du Niger est Niamey.",
  "Peux-tu me dire capitale du Niger ?": "La capitale du Niger est Niamey.",
  "Je veux savoir capitale du Niger.": "La capitale du Niger est Niamey.",
  "Explique-moi capitale du Niger.": "La capitale du Niger est Niamey.",
  "Dis-moi capitale du Niger.": "La capitale du Niger est Niamey.",
  "Quelle est la réponse concernant capitale du Niger ?": "La capitale du Niger est Niamey.",
  "Tu sais capitale du Niger ?": "La capitale du Niger est Niamey.",
  "Donne-moi une information sur capitale du Niger.": "La capitale du Niger est Niamey.",
  "J’aimerais connaître capitale du Niger.": "La capitale du Niger est Niamey.",
  "Réponds à la question : capitale du Niger.": "La capitale du Niger est Niamey.",
  "capitale du Sénégal": "La capitale du Sénégal est Dakar.",
  "Peux-tu me dire capitale du Sénégal ?": "La capitale du Sénégal est Dakar.",
  "Je veux savoir capitale du Sénégal.": "La capitale du Sénégal est Dakar.",
  "Explique-moi capitale du Sénégal.": "La capitale du Sénégal est Dakar.",
  "Dis-moi capitale du Sénégal.": "La capitale du Sénégal est Dakar.",
  "Quelle est la réponse concernant capitale du Sénégal ?": "La capitale du Sénégal est Dakar.",
  "Tu sais capitale du Sénégal ?": "La capitale du Sénégal est Dakar.",
  "Donne-moi une information sur capitale du Sénégal.": "La capitale du Sénégal est Dakar.",
  "J’aimerais connaître capitale du Sénégal.": "La capitale du Sénégal est Dakar.",
  "Réponds à la question : capitale du Sénégal.": "La capitale du Sénégal est Dakar.",
  "capitale du Togo": "La capitale du Togo est Lomé.",
  "Peux-tu me dire capitale du Togo ?": "La capitale du Togo est Lomé.",
  "Je veux savoir capitale du Togo.": "La capitale du Togo est Lomé.",
  "Explique-moi capitale du Togo.": "La capitale du Togo est Lomé.",
  "Dis-moi capitale du Togo.": "La capitale du Togo est Lomé.",
  "Quelle est la réponse concernant capitale du Togo ?": "La capitale du Togo est Lomé.",
  "Tu sais capitale du Togo ?": "La capitale du Togo est Lomé.",
  "Donne-moi une information sur capitale du Togo.": "La capitale du Togo est Lomé.",
  "J’aimerais connaître capitale du Togo.": "La capitale du Togo est Lomé.",
  "Réponds à la question : capitale du Togo.": "La capitale du Togo est Lomé.",
  "capitale de la Côte d’Ivoire": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Peux-tu me dire capitale de la Côte d’Ivoire ?": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Je veux savoir capitale de la Côte d’Ivoire.": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Explique-moi capitale de la Côte d’Ivoire.": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Dis-moi capitale de la Côte d’Ivoire.": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Quelle est la réponse concernant capitale de la Côte d’Ivoire ?": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Tu sais capitale de la Côte d’Ivoire ?": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Donne-moi une information sur capitale de la Côte d’Ivoire.": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "J’aimerais connaître capitale de la Côte d’Ivoire.": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "Réponds à la question : capitale de la Côte d’Ivoire.": "La capitale politique de la Côte d’Ivoire est Yamoussoukro.",
  "capitale du Nigeria": "La capitale du Nigeria est Abuja.",
  "Peux-tu me dire capitale du Nigeria ?": "La capitale du Nigeria est Abuja.",
  "Je veux savoir capitale du Nigeria.": "La capitale du Nigeria est Abuja.",
  "Explique-moi capitale du Nigeria.": "La capitale du Nigeria est Abuja.",
  "Dis-moi capitale du Nigeria.": "La capitale du Nigeria est Abuja.",
  "Quelle est la réponse concernant capitale du Nigeria ?": "La capitale du Nigeria est Abuja.",
  "Tu sais capitale du Nigeria ?": "La capitale du Nigeria est Abuja.",
  "Donne-moi une information sur capitale du Nigeria.": "La capitale du Nigeria est Abuja.",
  "J’aimerais connaître capitale du Nigeria.": "La capitale du Nigeria est Abuja.",
  "Réponds à la question : capitale du Nigeria.": "La capitale du Nigeria est Abuja.",
  "capitale de la France": "La capitale de la France est Paris.",
  "Peux-tu me dire capitale de la France ?": "La capitale de la France est Paris.",
  "Je veux savoir capitale de la France.": "La capitale de la France est Paris.",
  "Explique-moi capitale de la France.": "La capitale de la France est Paris.",
  "Dis-moi capitale de la France.": "La capitale de la France est Paris.",
  "Quelle est la réponse concernant capitale de la France ?": "La capitale de la France est Paris.",
  "Tu sais capitale de la France ?": "La capitale de la France est Paris.",
  "Donne-moi une information sur capitale de la France.": "La capitale de la France est Paris.",
  "J’aimerais connaître capitale de la France.": "La capitale de la France est Paris.",
  "Réponds à la question : capitale de la France.": "La capitale de la France est Paris.",
  "capitale de l’Allemagne": "La capitale de l’Allemagne est Berlin.",
  "Peux-tu me dire capitale de l’Allemagne ?": "La capitale de l’Allemagne est Berlin.",
  "Je veux savoir capitale de l’Allemagne.": "La capitale de l’Allemagne est Berlin.",
  "Explique-moi capitale de l’Allemagne.": "La capitale de l’Allemagne est Berlin.",
  "Dis-moi capitale de l’Allemagne.": "La capitale de l’Allemagne est Berlin.",
  "Quelle est la réponse concernant capitale de l’Allemagne ?": "La capitale de l’Allemagne est Berlin.",
  "Tu sais capitale de l’Allemagne ?": "La capitale de l’Allemagne est Berlin.",
  "Donne-moi une information sur capitale de l’Allemagne.": "La capitale de l’Allemagne est Berlin.",
  "J’aimerais connaître capitale de l’Allemagne.": "La capitale de l’Allemagne est Berlin.",
  "Réponds à la question : capitale de l’Allemagne.": "La capitale de l’Allemagne est Berlin.",
  "capitale de l’Espagne": "La capitale de l’Espagne est Madrid.",
  "Peux-tu me dire capitale de l’Espagne ?": "La capitale de l’Espagne est Madrid.",
  "Je veux savoir capitale de l’Espagne.": "La capitale de l’Espagne est Madrid.",
  "Explique-moi capitale de l’Espagne.": "La capitale de l’Espagne est Madrid.",
  "Dis-moi capitale de l’Espagne.": "La capitale de l’Espagne est Madrid.",
  "Quelle est la réponse concernant capitale de l’Espagne ?": "La capitale de l’Espagne est Madrid.",
  "Tu sais capitale de l’Espagne ?": "La capitale de l’Espagne est Madrid.",
  "Donne-moi une information sur capitale de l’Espagne.": "La capitale de l’Espagne est Madrid.",
  "J’aimerais connaître capitale de l’Espagne.": "La capitale de l’Espagne est Madrid.",
  "Réponds à la question : capitale de l’Espagne.": "La capitale de l’Espagne est Madrid.",
  "capitale de l’Italie": "La capitale de l’Italie est Rome.",
  "Peux-tu me dire capitale de l’Italie ?": "La capitale de l’Italie est Rome.",
  "Je veux savoir capitale de l’Italie.": "La capitale de l’Italie est Rome.",
  "Explique-moi capitale de l’Italie.": "La capitale de l’Italie est Rome.",
  "Dis-moi capitale de l’Italie.": "La capitale de l’Italie est Rome.",
  "Quelle est la réponse concernant capitale de l’Italie ?": "La capitale de l’Italie est Rome.",
  "Tu sais capitale de l’Italie ?": "La capitale de l’Italie est Rome.",
  "Donne-moi une information sur capitale de l’Italie.": "La capitale de l’Italie est Rome.",
  "J’aimerais connaître capitale de l’Italie.": "La capitale de l’Italie est Rome.",
  "Réponds à la question : capitale de l’Italie.": "La capitale de l’Italie est Rome.",
  "capitale du Canada": "La capitale du Canada est Ottawa.",
  "Peux-tu me dire capitale du Canada ?": "La capitale du Canada est Ottawa.",
  "Je veux savoir capitale du Canada.": "La capitale du Canada est Ottawa.",
  "Explique-moi capitale du Canada.": "La capitale du Canada est Ottawa.",
  "Dis-moi capitale du Canada.": "La capitale du Canada est Ottawa.",
  "Quelle est la réponse concernant capitale du Canada ?": "La capitale du Canada est Ottawa.",
  "Tu sais capitale du Canada ?": "La capitale du Canada est Ottawa.",
  "Donne-moi une information sur capitale du Canada.": "La capitale du Canada est Ottawa.",
  "J’aimerais connaître capitale du Canada.": "La capitale du Canada est Ottawa.",
  "Réponds à la question : capitale du Canada.": "La capitale du Canada est Ottawa.",
  "capitale des États-Unis": "La capitale des États-Unis est Washington, D.C.",
  "Peux-tu me dire capitale des États-Unis ?": "La capitale des États-Unis est Washington, D.C.",
  "Je veux savoir capitale des États-Unis.": "La capitale des États-Unis est Washington, D.C.",
  "Explique-moi capitale des États-Unis.": "La capitale des États-Unis est Washington, D.C.",
  "Dis-moi capitale des États-Unis.": "La capitale des États-Unis est Washington, D.C.",
  "Quelle est la réponse concernant capitale des États-Unis ?": "La capitale des États-Unis est Washington, D.C.",
  "Tu sais capitale des États-Unis ?": "La capitale des États-Unis est Washington, D.C.",
  "Donne-moi une information sur capitale des États-Unis.": "La capitale des États-Unis est Washington, D.C.",
  "J’aimerais connaître capitale des États-Unis.": "La capitale des États-Unis est Washington, D.C.",
  "Réponds à la question : capitale des États-Unis.": "La capitale des États-Unis est Washington, D.C.",
  "capitale du Japon": "La capitale du Japon est Tokyo.",
  "Peux-tu me dire capitale du Japon ?": "La capitale du Japon est Tokyo.",
  "Je veux savoir capitale du Japon.": "La capitale du Japon est Tokyo.",
  "Explique-moi capitale du Japon.": "La capitale du Japon est Tokyo.",
  "Dis-moi capitale du Japon.": "La capitale du Japon est Tokyo.",
  "Quelle est la réponse concernant capitale du Japon ?": "La capitale du Japon est Tokyo.",
  "Tu sais capitale du Japon ?": "La capitale du Japon est Tokyo.",
  "Donne-moi une information sur capitale du Japon.": "La capitale du Japon est Tokyo.",
  "J’aimerais connaître capitale du Japon.": "La capitale du Japon est Tokyo.",
  "Réponds à la question : capitale du Japon.": "La capitale du Japon est Tokyo.",
  "capitale de la Chine": "La capitale de la Chine est Pékin.",
  "Peux-tu me dire capitale de la Chine ?": "La capitale de la Chine est Pékin.",
  "Je veux savoir capitale de la Chine.": "La capitale de la Chine est Pékin.",
  "Explique-moi capitale de la Chine.": "La capitale de la Chine est Pékin.",
  "Dis-moi capitale de la Chine.": "La capitale de la Chine est Pékin.",
  "Quelle est la réponse concernant capitale de la Chine ?": "La capitale de la Chine est Pékin.",
  "Tu sais capitale de la Chine ?": "La capitale de la Chine est Pékin.",
  "Donne-moi une information sur capitale de la Chine.": "La capitale de la Chine est Pékin.",
  "J’aimerais connaître capitale de la Chine.": "La capitale de la Chine est Pékin.",
  "Réponds à la question : capitale de la Chine.": "La capitale de la Chine est Pékin.",
  "formule de l’eau": "La formule chimique de l’eau est H₂O.",
  "Peux-tu me dire formule de l’eau ?": "La formule chimique de l’eau est H₂O.",
  "Je veux savoir formule de l’eau.": "La formule chimique de l’eau est H₂O.",
  "Explique-moi formule de l’eau.": "La formule chimique de l’eau est H₂O.",
  "Dis-moi formule de l’eau.": "La formule chimique de l’eau est H₂O.",
  "Quelle est la réponse concernant formule de l’eau ?": "La formule chimique de l’eau est H₂O.",
  "Tu sais formule de l’eau ?": "La formule chimique de l’eau est H₂O.",
  "Donne-moi une information sur formule de l’eau.": "La formule chimique de l’eau est H₂O.",
  "J’aimerais connaître formule de l’eau.": "La formule chimique de l’eau est H₂O.",
  "Réponds à la question : formule de l’eau.": "La formule chimique de l’eau est H₂O.",
  "symbole de l’oxygène": "Le symbole chimique de l’oxygène est O.",
  "Peux-tu me dire symbole de l’oxygène ?": "Le symbole chimique de l’oxygène est O.",
  "Je veux savoir symbole de l’oxygène.": "Le symbole chimique de l’oxygène est O.",
  "Explique-moi symbole de l’oxygène.": "Le symbole chimique de l’oxygène est O.",
  "Dis-moi symbole de l’oxygène.": "Le symbole chimique de l’oxygène est O.",
  "Quelle est la réponse concernant symbole de l’oxygène ?": "Le symbole chimique de l’oxygène est O.",
  "Tu sais symbole de l’oxygène ?": "Le symbole chimique de l’oxygène est O.",
  "Donne-moi une information sur symbole de l’oxygène.": "Le symbole chimique de l’oxygène est O.",
  "J’aimerais connaître symbole de l’oxygène.": "Le symbole chimique de l’oxygène est O.",
  "Réponds à la question : symbole de l’oxygène.": "Le symbole chimique de l’oxygène est O.",
  "symbole du carbone": "Le symbole chimique du carbone est C.",
  "Peux-tu me dire symbole du carbone ?": "Le symbole chimique du carbone est C.",
  "Je veux savoir symbole du carbone.": "Le symbole chimique du carbone est C.",
  "Explique-moi symbole du carbone.": "Le symbole chimique du carbone est C.",
  "Dis-moi symbole du carbone.": "Le symbole chimique du carbone est C.",
