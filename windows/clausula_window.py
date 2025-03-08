import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data.data import load_data  # Reutilizamos la función de carga de datos

def app():
    st.title("Jugadores por Cláusula de Salida")
    st.markdown("---")

    df = load_data()

    if df is not None:
        if "Release Clause(£)" in df.columns:
            # Ordenamos y tomamos los 15 jugadores con mayor cláusula de salida
            df_sorted = df.sort_values("Release Clause(£)", ascending=False).head(15)

            fig, ax = plt.subplots(figsize=(12, 6))
            ax.bar(df_sorted["Name"], df_sorted["Release Clause(£)"], color="blue")
            ax.set_xlabel("Jugador")
            ax.set_ylabel("Cláusula de salida")
            ax.set_title("Top 15 Jugadores por Cláusula de salida")
            ax.tick_params(axis="x", rotation=45)
            st.pyplot(fig)
        else:
            st.error("La columna 'Release Clause(£)' no existe en el dataset.")
    else:
        st.write("No se pueden mostrar los datos.")
