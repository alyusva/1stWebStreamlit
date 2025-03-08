import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data.data import load_data  # Importamos la función de carga de datos

def app():
    # Encabezado con logos
    header_col1, header_col2 = st.columns([1, 1])
    with header_col1:
        st.image("./src/img/ceu_logo.png", width=300)
    with header_col2:
        st.image("./src/img/laliga_logo.png", width=300)

    st.title("Estadísticas de la Liga de Fútbol :soccer:")
    st.markdown("---")

    df = load_data()

    if df is not None:
        # Barra lateral para filtros
        st.sidebar.header("Filtros")
        equipos = st.sidebar.multiselect(
            "Selecciona equipos:",
            options=df["Club"].unique(),
            default=df["Club"].unique(),
        )

        # Filtrar el dataframe
        df_filtered = df[df["Club"].isin(equipos)]

        # Mostrar datos filtrados
        st.write("### Datos Filtrados")
        st.dataframe(df_filtered)

        # Gráfica de puntuación por jugador (Top 20)
        st.write("### Puntuación de Jugador (Top 20)")
        top_20_mejores = df_filtered.nlargest(20, "Overall")

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(top_20_mejores["Name"], top_20_mejores["Overall"], color="green")
        ax.set_xlabel("Jugador")
        ax.set_ylabel("Puntuación")
        ax.set_title("Top 20 Mejores jugadores")
        ax.tick_params(axis="x", rotation=45)
        st.pyplot(fig)
    else:
        st.write("No se pueden mostrar los datos.")
