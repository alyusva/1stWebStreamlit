import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("./src/data/CLEAN_FIFA23_official_data.csv")
        return df
    except FileNotFoundError:
        st.error("Error: No se encontró el archivo CLEAN_FIFA23_official_data.csv en la ruta especificada.")
        return None
