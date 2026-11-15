import streamlit as st



def afficher_saisons(f1db_races_race_results):
    annee_saison=st.selectbox("Choisissez une saison", f1db_races_race_results["year"].unique())
    if annee_saison==False:
        return
    
    annee_choisie=f1db_races_race_results[f1db_races_race_results["year"]==annee_saison]
    annee_choisie["points"] = annee_choisie["points"].fillna(0)
    liste_pilotes_saison=annee_choisie["driverId"].unique()


    checkbox_pilotes={}
    colonnes_pilotes = st.columns(4)

    for index, pilote in enumerate(liste_pilotes_saison):
        with colonnes_pilotes[index % 4]:
            checkbox_pilotes[pilote] = st.checkbox(pilote)
    pilotes_choisis=[]
    for j in liste_pilotes_saison:
        if checkbox_pilotes[j]==True:
            pilotes_choisis.append(j)
    resultats_selectionnes = annee_choisie[annee_choisie["driverId"].isin(pilotes_choisis)]

    if len(pilotes_choisis)>0:
        bilan_saison=st.line_chart(resultats_selectionnes, x="round", y="points", color="driverId")
