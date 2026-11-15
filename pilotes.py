import streamlit as st

def afficher_pilotes(f1seasons_drivers, f1db_races_race_results):
    ###DATAFRAME###

    choix_annee=st.multiselect("Choisissez une ou plusieurs années", f1seasons_drivers["year"].sort_values(ascending=True).unique())
    pilotes_filtres=f1seasons_drivers[f1seasons_drivers["year"].isin(choix_annee)]
    if len(choix_annee)==0:
        return
    choix_pilote=st.multiselect("Choisissez un ou plusieurs pilote", pilotes_filtres["driverId"].sort_values(ascending=True).unique(), select_all=True)
    if len(choix_pilote)==0:
            return
    pilote_stats=f1seasons_drivers[f1seasons_drivers["driverId"].isin(choix_pilote)]
    pilote_stats=pilote_stats.groupby("driverId").agg(Nombre_course=("totalRaceStarts", "sum"), Nombre_victoires=("totalRaceWins", "sum"), Nombre_points=("totalPoints", "sum"), Nombre_podium=("totalPodiums", "sum"),
                                                            Meilleur_resultat=("bestRaceResult", "min"), Nombre_Pole=("totalPolePositions", "max"))
    pilote_stats["Points_par_course"]=((pilote_stats["Nombre_points"])/(pilote_stats["Nombre_course"])).round(2)
    st.dataframe(pilote_stats)

###BARRES###

    if len(choix_pilote)==0:
        return
    st.write("Selectionnez les statistiques à afficher dans le graphique en barres (carrière complète)")
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
    
    if nbvictoires==True or nbcourses==True or nbpoints == True or nbpodium == True or nbpole==True:
        stats_barres=st.bar_chart(pilote_stats, y=select_stats, stack=False)


    #########Tableau comparatif#########
    if len(choix_annee)==1:
        annee_saison=f1db_races_race_results[f1db_races_race_results["year"].isin(choix_annee)]
        resultat_gp=f1db_races_race_results["positionNumber"]
        resultat_pilote=annee_saison[annee_saison["driverId"].isin(choix_pilote)]
        tableau_resultat = resultat_pilote.pivot(
        index="round",
        columns="driverId",
        values="positionNumber"
        )
        tableau_resultat.index="Position course " + tableau_resultat.index.astype(str)
        st.write("Recapitulatif des positions à l'arrivée pour chaque manche de la saison sélectionnée:")
        st.dataframe(tableau_resultat)
    else:
       st.info("Pour comparer les résultats de deux pilotes, choisissez deux pilotes d'une même saison.")