import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

st.set_page_config(page_title="Prédiction Prix Immobilier", layout="centered")
st.title("🏠 Application de Prédiction Immobilière")
st.write("Bienvenue ! Cette application utilise un modèle de Machine Learning entraîné dans Snowflake.")

try:
    session = get_active_session()
    st.success("Connecté à Snowflake avec succès !")
except:
    st.error("Erreur de connexion à Snowflake.")
    st.stop()

# --- Formulaire de saisie ---
st.sidebar.header("Caractéristiques de la maison")

area            = st.sidebar.number_input("📐 Surface (sqft)",      min_value=500, max_value=20000, value=5000)
bedrooms        = st.sidebar.slider("🛏️  Chambres",                 1, 6, 3)
bathrooms       = st.sidebar.slider("🚿 Salles de bain",            1, 4, 1)
stories         = st.sidebar.slider("🏢 Étages",                    1, 4, 2)
parking         = st.sidebar.slider("🚗 Places de parking",         0, 3, 1)
mainroad        = st.sidebar.selectbox("🛣️  Route principale ?",    ["yes", "no"])
guestroom       = st.sidebar.selectbox("🛋️  Chambre d'amis ?",      ["yes", "no"])
basement        = st.sidebar.selectbox("🪜 Sous-sol ?",             ["yes", "no"])
hotwaterheating = st.sidebar.selectbox("🔥 Eau chaude sanitaire ?", ["yes", "no"])
airconditioning = st.sidebar.selectbox("❄️  Climatisation ?",        ["yes", "no"])
prefarea        = st.sidebar.selectbox("⭐ Zone préférentielle ?",  ["yes", "no"])
furnishing      = st.sidebar.selectbox("🛋️  Meublé ?",              ["furnished", "semi-furnished", "unfurnished"])

# --- Bouton de Prédiction ---
if st.button("💰 Estimer le prix", type="primary", use_container_width=True):

    def encode(val):
        return 1 if val == "yes" else 0

    def encode_furn(val):
        return {"furnished": 2, "semi-furnished": 1, "unfurnished": 0}[val]

    result = session.sql(f"""
        SELECT ML_SCHEMA.PREDICT_HOUSE_PRICE(
            {area}, {bedrooms}, {bathrooms}, {stories},
            {encode(mainroad)}, {encode(guestroom)}, {encode(basement)},
            {encode(hotwaterheating)}, {encode(airconditioning)},
            {parking}, {encode(prefarea)}, {encode_furn(furnishing)}
        ) AS PRIX_PREDIT
    """).collect()

    prediction = result[0]["PRIX_PREDIT"]

    st.success(f"### 💵 Prix estimé : {prediction:,.0f} €")
    st.balloons()

    with st.expander("📊 Récapitulatif de votre maison"):
        recap = pd.DataFrame({
            "Caractéristique": [
                "Surface", "Chambres", "Salles de bain", "Étages",
                "Route principale", "Chambre d'amis", "Sous-sol",
                "Eau chaude", "Climatisation", "Parking",
                "Zone préférentielle", "Meublé"
            ],
            "Valeur": [
                area, bedrooms, bathrooms, stories,
                mainroad, guestroom, basement,
                hotwaterheating, airconditioning, parking,
                prefarea, furnishing
            ]
        })
        st.dataframe(recap, hide_index=True, use_container_width=True)
