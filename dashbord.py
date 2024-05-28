import pandas as pd
import streamlit as st
import plotly.express as px
from scipy.stats import chi2_contingency

# Fonction pour charger les données
def load_data():
    return pd.read_excel('translated_data.xlsx')

# Charger les données
data = load_data()

# Application Streamlit
st.header('Résumé et Visualisation des Données')

# Afficher les données
st.header('Tableau de Données')
st.table(data.head())

# Statistiques descriptives
st.header('Statistiques Descriptives')
st.write(data.describe())

# Visualisations
st.header('Visualisations')

# Exemple de graphique 1 : Distribution des âges
if 'Age' in data.columns:
    fig_age = px.histogram(data, x='Age', title='Distribution des Âges')
    st.plotly_chart(fig_age)

# Exemple de graphique 2 : Répartition par genre
if 'Genre' in data.columns:
    fig_genre = px.pie(data, names='Genre', title='Répartition par Genre',)
    st.plotly_chart(fig_genre)

st.header('_Énergie propre et d’un coût abordable_ :blue[ODD-7] :sunglasses:', divider='rainbow')
# Replace null values with "No electricity"
data['PrincipalesSourcesEnergie'].fillna('No electricity', inplace=True)
# Bar chart for energy sources
energy_source_percentage = (data['PrincipalesSourcesEnergie'].value_counts() / len(data)) * 100
fig_energy_sources_percentage = px.bar(x=energy_source_percentage.index, 
                                       y=energy_source_percentage.values,
                                       labels={'x': 'Sources d\'Énergie', 'y': 'Pourcentage'},
                                       title='Répartition des Sources Principales d\'Énergie en Pourcentage')
st.plotly_chart(fig_energy_sources_percentage)
# Afficher le pourcentage de personnes avec accès à l'électricité
percentage_with_electricity = ((data['PrincipalesSourcesEnergie']=="Electricite").sum() / len(data)) * 100
st.write(f"Pourcentage de personnes avec accès à l'électricité : {percentage_with_electricity:.2f}%")
st.header('_Travail décent et croissance économique_ :blue[ODD-8]', divider='rainbow')
st.title('Tableau Croisé Genre-Activité Professionnelle')

# Créer le tableau croisé
cross_table = pd.crosstab(data['Genre'], data['Activite'])

# Afficher le tableau croisé
st.write(cross_table)

chi2, p_value, _, _ = chi2_contingency(cross_table)
st.write(f"Statistique du Chi-deux : {chi2}")
st.write(f"P-value : {p_value}")

# Interprétation des résultats
alpha = 0.1
if p_value < alpha:
    st.write(f"La p-value est inférieure au seuil {alpha} de 0.05, donc on rejette l'hypothèse nulle.")
    st.write("Il y a une association significative entre le genre et l'activité professionnelle.")
else:
    st.write(f"La p-value est supérieure au seuil {alpha} de 0.05, donc on ne peut pas rejeter l'hypothèse nulle.")
    st.write("Il n'y a pas suffisamment de preuves pour conclure à une association significative entre le genre et l'activité professionnelle.")

st.header('_Industrie, innovation et infrastructure_ :orange[ODD-9]', divider='red')
st.title('Distribution de l\'Accès aux Réseaux Mobiles dans la Région')

# Pie chart for mobile network access
fig_mobile_access = px.pie(data, 
                           names='OperateurMobile', 
                           title='Distribution de l\'Accès aux Réseaux Mobiles dans la Région',
                           labels={'OperateurMobile': 'Opérateur Mobile'})
st.plotly_chart(fig_mobile_access)

percentage_operators = (data['OperateurMobile'].value_counts(normalize=True) * 100).round(2)
st.write(f"""
    Ce diagramme circulaire illustre la distribution de l'accès aux réseaux mobiles dans la région. Chaque secteur représente la part de marché de chaque opérateur mobile parmi la population.
    
    Voici les pourcentages de chaque opérateur mobile :
    - {percentage_operators.index[0]} : {percentage_operators.iloc[0]}%
    - {percentage_operators.index[1]} : {percentage_operators.iloc[1]}%
""")
def group_distance(distance):
    if distance > 2:
        return 'Oui'
    else:
        return 'Non'
data['DistanceRoutePraticable'] = data['DistanceRoutePraticable'].apply(group_distance)
fig_distance_to_roads = px.histogram(data, 
                                     x='DistanceRoutePraticable', 
                                     title='Distribution de la Population Vivant à Proximité des Routes Praticables Toute l\'Année',
                                     labels={'DistanceRoutePraticable': 'Distance à la Route Praticable (km)', 'count': 'Nombre de Personnes'})
st.plotly_chart(fig_distance_to_roads)
# Afficher le pourcentage de personnes vivant près des routes praticables
percentage_nearby_roads = (data['DistanceRoutePraticable'].value_counts(normalize=True) * 100).round(2)
st.write(f"Pourcentage de personnes vivant près des routes praticables :")
st.write(f"- Oui : {percentage_nearby_roads['Oui']}%")
st.write(f"- Non : {percentage_nearby_roads['Non']}%")

#### ODD 10

st.header('_Réduction des inégalités_ :blue[ODD-10]', divider='blue')

#### ODD 11

st.header('_Villes et communautés durables_ :blue[ODD-11]', divider='rainbow')

# Streamlit app
st.title('Tableau Croisé de la Qualité du Logement selon le Milieu de Vie')

# Assign housing quality based on neighborhood evaluation
data['QualiteLogement'] = data['EvaluationQuartier'].apply(lambda x: 'Bonne' if x > 5 else 'Mauvaise')

# Create cross table
cross_table = pd.crosstab(data['MilieuVie'], data['QualiteLogement'])

# Display cross table
st.write('Tableau Croisé de la Qualité du Logement selon le Milieu de Vie :')
st.write(cross_table)



st.header('_Consommation et production responsables_ :blue[ODD-12]', divider='violet')
st.title('Distribution des Méthodes d\'Élimination des Déchets')

# Diagramme circulaire pour les méthodes d'élimination des déchets
fig_elimination_methods = px.pie(data, 
                                 names='MethodeElimination', 
                                 title='Distribution des Méthodes d\'Élimination des Déchets',
                                 labels={'MethodeElimination': 'Méthode d\'Élimination'})
st.plotly_chart(fig_elimination_methods)
percentage_elimination_methods = (data['MethodeElimination'].value_counts(normalize=True) * 100).round(2)
st.write(f"""
    Ce diagramme circulaire illustre la distribution des méthodes d'élimination des déchets dans la région.
    
    Voici les pourcentages de chaque méthode d'élimination :
    - Poubelle communale : {percentage_elimination_methods['Poubelle communale']}%
    - Camion de collecte : {percentage_elimination_methods['Camion de collecte']}%
    - Autre : {percentage_elimination_methods['Autre']}%
    - Décharge à ciel ouvert : {percentage_elimination_methods['Décharge à ciel ouvert']}%
    """)

# Save as static HTML

