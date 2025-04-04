
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Mauro Ferrari", layout="wide")
st.title("📊 Dashboard Mauro Ferrari")

# Carica i file CSV
eventi = pd.read_csv("eventi_unificati.csv", parse_dates=["data"])

# Filtri dinamici
agenti = eventi["NOME"].dropna().unique().tolist()
mesi = sorted(eventi["data"].dt.to_period("M").astype(str).unique().tolist())

col1, col2 = st.columns(2)
agente_sel = col1.selectbox("👤 Seleziona agente", ["Tutti"] + agenti)
mese_sel = col2.selectbox("🗓️ Seleziona mese", ["Tutti"] + mesi)

# Applica filtri
df = eventi.copy()
if agente_sel != "Tutti":
    df = df[df["NOME"] == agente_sel]
if mese_sel != "Tutti":
    df = df[df["data"].dt.to_period("M").astype(str) == mese_sel]

# Statistiche chiave
col1, col2, col3 = st.columns(3)
col1.metric("📋 Totale Eventi", len(df))
col2.metric("👥 Clienti coinvolti", df['COGNOME'].nunique())
col3.metric("🏘️ Immobili trattati", df['CODICE'].nunique())

# Grafico eventi per tipo
st.subheader("📈 Eventi per tipologia")
tipologia_counts = df['NOME_y'].value_counts().reset_index()
tipologia_counts.columns = ['Tipologia', 'Conteggio']
st.bar_chart(tipologia_counts.set_index('Tipologia'))

# Tabella dettagli
st.subheader("📋 Dettaglio eventi")
st.dataframe(df[['data', 'NOME_y', 'COGNOME', 'NOME_CLIENTE', 'CODICE', 'NOME']].rename(columns={
    'data': 'Data',
    'NOME_y': 'Tipologia',
    'COGNOME': 'Cliente (Cognome)',
    'NOME_CLIENTE': 'Cliente (Nome)',
    'CODICE': 'Codice immobile',
    'NOME': 'Agente'
}))
