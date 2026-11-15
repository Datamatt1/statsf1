import streamlit as st

def afficher_circuits(circuits_complets):
    pays_circuit=st.selectbox("Choisissez un pays", circuits_complets["countryId"].sort_values(ascending=True).unique())
    filtre_circuit=circuits_complets[circuits_complets["countryId"]==pays_circuit]
    filtre_circuit["nom_complet"] = filtre_circuit["fullName"] + " - " + filtre_circuit["id_y"].astype(str)     ###Choix du pays puis du circuit
    pays_circuits2=st.selectbox("Choisissez un circuit", filtre_circuit["nom_complet"])
    circuit_selectionne=filtre_circuit[filtre_circuit["nom_complet"]==pays_circuits2]
    
    
    image_circuit=circuit_selectionne["id_y"].iloc[0]
    st.image(f"https://raw.githubusercontent.com/f1db/f1db/refs/heads/main/src/assets/circuits/black-outline/{image_circuit}.svg")  #Image du circuit
        
        
    st.write("Pays : ", circuit_selectionne["countryId"].iloc[0])
    st.write("Ville :", circuit_selectionne["placeName"].iloc[0])             ##Stats du circuit
    st.write("Longueur :", circuit_selectionne["length_y"].iloc[0], "km")
    st.write("Virages :", circuit_selectionne["turns_y"].iloc[0])
    st.write("Nombre de courses courues sur ce circuit (tous tracés confondus) : ", circuit_selectionne["totalRacesHeld"].iloc[0])
    if circuit_selectionne["effective"].iloc[0]==True:
       st.write("Configuration actuelle")
    else:
         st.write("Configuration historique")
    
