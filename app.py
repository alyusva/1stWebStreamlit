import streamlit as st
from windows import main_window, clausula_window

# Configuración de la página
st.set_page_config(
    page_title="Estadísticas de Fútbol",
    page_icon=":soccer:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estado de la ventana actual (default: vista principal)
if "view" not in st.session_state:
    st.session_state.view = "main"

# Botón para alternar vista
if st.button("Cambiar vista"):
    st.session_state.view = "clausula" if st.session_state.view == "main" else "main"

# Renderizar la vista según el estado
if st.session_state.view == "clausula":
    clausula_window.app()
else:
    main_window.app()
