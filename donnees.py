import pandas as pd
import streamlit as st

@st.cache_data
def charger_donnees():

    # Import CSV
    f1seasons_drivers = pd.read_csv("f1db-seasons-drivers.csv")
    f1db_circuits = pd.read_csv("f1db-circuits.csv")
    f1db_races_race_results = pd.read_csv("f1db-races-race-results.csv")
    f1db_races = pd.read_csv("f1db-races.csv")
    f1db_detail_circuit = pd.read_csv("f1db-circuits-layouts.csv")

    # Jointure
    circuits_complets = f1db_circuits.merge(
        f1db_detail_circuit,
        left_on="id",
        right_on="circuitId",
        how="left"
    )

    return f1seasons_drivers, f1db_races_race_results, circuits_complets