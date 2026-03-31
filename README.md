# MBAESG_2025_CLASSE_A_EVALUATION_DATAENGINEER_MLOPS
Projet Snowflake &amp; Machine Learning - Prédiction des prix des maisons

## 👥 Membres du groupe
*   **SALIMI MAZRAG AMINA** (Chef de Projet & Data Analyst)
*   **ELMAN NAJOUA** (Data Engineer / Scientist)
*   **ELFATHI HAJAR** (Data Engineer / Scientist)

## 📝 Description du Projet
Ce projet consiste à développer un pipeline complet de **Machine Learning** directement au sein de la plateforme **Snowflake**. L'objectif est de construire un modèle prédictif capable d'estimer le prix de vente des propriétés immobilières en fonction de diverses caractéristiques (surface, nombre de chambres, climatisation, etc.).

L'ensemble du workflow est réalisé sans extraction de données, en utilisant les capacités de calcul de Snowflake et de Snowpark.

## 🛠️ Technologies utilisées
*   **Snowflake** : Plateforme de données cloud et moteur de calcul.
*   **Snowpark** : Pour la manipulation des données en Python.
*   **Snowflake ML & Model Registry** : Pour l'entraînement, l'optimisation et la gestion des versions du modèle.
*   **Streamlit** : Pour la création d'une application interactive de prédiction.

## 🚀 Étapes du Workshop
1.  **Ingestion et Exploration (EDA)** : Chargement des données depuis S3 et analyse des corrélations entre les variables.
2.  **Préparation des données** : Nettoyage, encodage des variables catégorielles et normalisation.
3.  **Entraînement du modèle** : Utilisation de bibliothèques ML (Scikit-learn / XGBoost) pour entraîner les modèles.
4.  **Évaluation et Optimisation** : Calcul des métriques de performance (Accuracy, RMSE, MAE) et réglage des hyperparamètres (Grid Search).
5.  **Gouvernance (Model Registry)** : Enregistrement du meilleur modèle dans le registre Snowflake pour la mise en production.
6.  **Inférence et Application** : Développement d'une application Streamlit permettant aux utilisateurs de saisir des caractéristiques de maison et d'obtenir un prix estimé en temps réel.

## 📂 Structure du dépôt
*   `/notebooks` : Contient le Notebook Snowflake avec l'intégralité du pipeline ML.
*   `/app` : Code source de l'application Streamlit.
*   `README.md` : Documentation du projet.

## 📊 Description du Dataset
Le dataset contient des informations clés sur les caractéristiques des habitations. Voici le détail des variables :

*   **price** : Prix de vente de la maison (Variable cible).
*   **area** : Surface totale en mètres carrés.
*   **bedrooms** : Nombre de chambres.
*   **bathrooms** : Nombre de salles de bain.
*   **stories** : Nombre d'étages.
*   **mainroad** : Accès à une route principale (OUI/NON).
*   **guestroom** : Présence d'une chambre d'amis (OUI/NON).
*   **basement** : Présence d'un sous-sol (OUI/NON).
*   **hotwaterheating** : Présence d'un chauffage à eau chaude (OUI/NON).
*   **airconditioning** : Présence de la climatisation (OUI/NON).
*   **parking** : Nombre de places de stationnement.
*   **prefarea** : Située dans une zone privilégiée (OUI/NON).
*   **furnishingstatus** : État d'ameublement (meublé, semi-meublé, non meublé).
