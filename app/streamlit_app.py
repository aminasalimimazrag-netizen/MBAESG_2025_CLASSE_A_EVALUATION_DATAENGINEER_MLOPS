
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Configuration de la page
st.set_page_config(page_title="Prédiction Prix Immobilier", layout="centered")

st.title("🏠 Application de Prédiction Immobilière")
st.write("Bienvenue ! Cette application utilise un modèle de Machine Learning entraîné dans Snowflake.")

# Connexion à Snowflake (automatique dans Snowflake Notebooks/Streamlit)
try:
    session = get_active_session()
    st.success("Connecté à Snowflake avec succès !")
except:
    st.error("Erreur de connexion à Snowflake.")

# --- Formulaire de saisie pour l'utilisateur ---
st.sidebar.header("Caractéristiques de la maison")

area = st.sidebar.number_input("Surface (Area m²)", min_value=500, max_value=20000, value=5000)
bedrooms = st.sidebar.slider("Nombre de chambres", 1, 6, 3)
bathrooms = st.sidebar.slider("Nombre de salles de bain", 1, 4, 1)
airconditioning = st.sidebar.selectbox("Climatisation", ["yes", "no"])

# --- Bouton de Prédiction ---
if st.button("Estimer le prix"):
    # Note pour l'équipe : Ici, on appellera le modèle enregistré dans le Model Registry
    st.info("Le modèle sera appelé ici une fois l'entraînement terminé par les Data Scientists.")
    st.write(f"Données saisies : {area}m², {bedrooms} ch, {bathrooms} sdb, Clim: {airconditioning}")
