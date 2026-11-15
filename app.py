import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

from pilotes import afficher_pilotes
from circuits import afficher_circuits

from donnees import charger_donnees
f1seasons_drivers, f1db_races_race_results, circuits_complets = charger_donnees()


###Titre et menu###
st.title("🏎️ F1 Dashboard 🏎️")

st.sidebar.title("Menu")
with st.sidebar:
 selected_page = option_menu(
    menu_title="Sections", # Titre du menu (ou None)
    options=["Accueil", "Pilotes", "Circuits"],
    icons=["house", "person", "flag-fill"],
    default_index=0
 )





if selected_page=="Accueil":
    st.write("Bienvenue sur ma page de statistique sur la Formule 1\n\n" \
    "Je crée ce dashboard dans le cadre de ma formation de Data Analyst afin de m'entraîner à maîtriser" \
    "python et ses différentes librairies. \n\n" \
    "J'ai utilisé la base de données [F1DB](https://github.com/f1db/f1db)")



elif selected_page=="Pilotes":
   afficher_pilotes(f1seasons_drivers, f1db_races_race_results)



elif selected_page=="Circuits":  
    afficher_circuits(circuits_complets)