import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

f1seasons_drivers=pd.read_csv("f1db-seasons-drivers.csv") ##Import du csv
f1db_circuits=pd.read_csv("f1db-circuits.csv")
f1db_races_race_results=pd.read_csv("f1db-races-race-results.csv")
f1db_races=pd.read_csv("f1db-races.csv")
st.title("🏎️ F1 Dashboard 🏎️")

st.sidebar.title("Menu")
with st.sidebar:
 selected_page = option_menu(
    menu_title="Sections", # Titre du menu (ou None)
    options=["Accueil", "Pilotes", "Circuits"],
    icons=["house", "person", "flag-fill"],
    default_index=0
 )
saisons_selectionnees=f1seasons_drivers[f1seasons_drivers["year"]>2024] ##Uniquement les saisons 2025/2026



if selected_page=="Accueil":
    st.write("Bienvenue sur ma page de statistique sur la Formule 1\n\n" \
    "Je crée ce dashboard dans le cadre de ma formation de Data Analyst afin de m'entraîner à maîtriser" \
    "python et ses différentes librairies. \n\n" \
    "J'ai utilisé la base de données [F1DB](https://github.com/f1db/f1db)")



elif selected_page=="Pilotes":


###DATAFRAME###

    choix_annee=st.multiselect("Choisissez une ou plusieurs années", f1seasons_drivers["year"].sort_values(ascending=True).unique())
    pilotes_filtres=f1seasons_drivers[f1seasons_drivers["year"].isin(choix_annee)]
    choix_pilote=st.multiselect("Choisissez un ou plusieurs pilote", pilotes_filtres["driverId"].sort_values(ascending=True).unique(), select_all=True)
    pilote_stats=f1seasons_drivers[f1seasons_drivers["driverId"].isin(choix_pilote)]
    pilote_stats=pilote_stats.groupby("driverId").agg(Nombre_course=("totalRaceStarts", "sum"), Nombre_victoires=("totalRaceWins", "sum"), Nombre_points=("totalPoints", "sum"), Nombre_podium=("totalPodiums", "sum"),
                                                        Meilleur_resultat=("bestRaceResult", "min"), Nombre_Pole=("totalPolePositions", "max"))
    pilote_stats["Points_par_course"]=((pilote_stats["Nombre_points"])/(pilote_stats["Nombre_course"])).round(2)
    st.dataframe(pilote_stats)

###BARRES###

    st.write("Selectionnez les statistiques à afficher dans le graphique en barres")
    col1, col2, col3, col4, col5 = st.columns(5)  ##Nombre de colonnes pour les checkbox

    select_stats=[]
    with col1:
        nbvictoires=st.checkbox("Nombre de victoires")
    with col2:
        nbcourses=st.checkbox("Nombre de courses")
    with col3:
       nbpoints=st.checkbox("Nombre de points marqués")    #1 with = 1 colonne
    with col4: 
       nbpodium=st.checkbox("Nombre de podiums")
    with col5:
       nbpole=st.checkbox("Nombre de poles positions")



    if nbvictoires==True:
       select_stats.append("Nombre_victoires")
    if nbcourses==True:
       select_stats.append("Nombre_course")
    if nbpoints==True:
       select_stats.append("Nombre_points")   #les checkbox
    if nbpodium==True:
       select_stats.append("Nombre_podium")
    if nbpole==True:
       select_stats.append("Nombre_Pole")
    

    stats_barres=st.bar_chart(pilote_stats, y=select_stats, stack=False)


    #########Courbe#########
    annee_saison=f1db_races_race_results[f1db_races_race_results["year"].isin(choix_annee)]
    resultat_gp=f1db_races_race_results["positionNumber"]
    resultat_pilote=annee_saison[annee_saison["driverId"].isin(choix_pilote)]
    tableau_resultat = resultat_pilote.pivot(
    index="round",
    columns="driverId",
    values="positionNumber"
    )
    tableau_resultat.index="Résultat course " + tableau_resultat.index.astype(str)
    st.dataframe(tableau_resultat)

elif selected_page=="Circuits":
 st.write("attente de creation")