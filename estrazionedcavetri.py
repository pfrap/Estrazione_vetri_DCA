import streamlit as st
from Funzione_csv import *

st.set_page_config(layout="wide")

st.title("Elaborazione estrazione vetri DCA")
st.write(
    "Caricare csv, DCA")

uploaded_file = st.file_uploader("Carica file CSV estratto da Autocad senza elaborazioni "
"(grezzo), dopo elaborazione puoi scaricare Excel.", type=["csv"])
if uploaded_file is not None:
    df=carica_csv(uploaded_file)
    st.dataframe(df)