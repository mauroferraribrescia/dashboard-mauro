
import streamlit as st
import pandas as pd

# Carica il CSV
df = pd.read_csv('eventi_2025_Q1.csv')

# Mostra il dataset nella dashboard
st.title("Analisi Eventi 2025 - Q1")
st.write(df)

# Analisi: conteggio eventi per tipo (per agente)
tipologia_counts = df['Agente'].value_counts().reset_index()
tipologia_counts.columns = ['Agente', 'Numero di Eventi']
st.subheader("Eventi per Agente")
st.write(tipologia_counts)

# Grafico a barre degli eventi per agente
st.bar_chart(tipologia_counts.set_index('Agente')['Numero di Eventi'])
