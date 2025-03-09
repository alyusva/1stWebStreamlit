# Estadísticas de Fútbol ⚽

Una aplicación web desarrollada con Streamlit que visualiza y analiza datos de jugadores de fútbol de FIFA 23.

![logos](./src/img/laliga_logo.png)

## 📋 Descripción

Esta aplicación permite explorar estadísticas de jugadores de fútbol de FIFA 23, proporcionando diferentes visualizaciones y filtros para analizar datos como:

- Puntuaciones generales de jugadores
- Cláusulas de rescisión
- Estadísticas por equipo
- Y más...

La aplicación cuenta con una interfaz intuitiva que permite alternar entre diferentes vistas para analizar distintos aspectos de los datos.

## 🚀 Características

- **Vista Principal**: Muestra estadísticas generales y el top 20 de jugadores por puntuación
- **Vista de Cláusula**: Visualiza los 15 jugadores con las cláusulas de rescisión más altas
- **Filtros interactivos**: Permite filtrar por equipos específicos
- **Datos actualizados**: Utiliza la base de datos oficial de FIFA 23
- **Interfaz intuitiva**: Cambio sencillo entre vistas con un solo clic

## 🔧 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/estadisticas-futbol.git
   cd estadisticas-futbol
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## 📂 Estructura del Proyecto

```
.
├── app.py                  # Controlador principal y gestor de navegación
├── requirements.txt        # Dependencias del proyecto
├── src
│   ├── data
│   │   ├── data.py                 # Función para cargar y cachear el dataset
│   │   └── CLEAN_FIFA23_official_data.csv
│   └── img
│       ├── ceu_logo.png
│       └── laliga_logo.png
└── windows                 # Módulos de las distintas vistas
    ├── main_window.py      # Vista principal (estadísticas generales)
    └── clausula_window.py  # Vista alternativa (gráfico de Cláusula de salida)
```

## 💻 Uso

1. Al iniciar la aplicación, se muestra la vista principal con estadísticas generales.
2. Utiliza el botón "Cambiar vista" para alternar entre la vista principal y la vista de cláusulas de rescisión.
3. En la barra lateral, selecciona los equipos que deseas analizar.
4. Explora los gráficos interactivos y la información mostrada.

## 🛠️ Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) - Framework para crear aplicaciones web de datos
- [Pandas](https://pandas.pydata.org/) - Análisis de datos
- [Matplotlib](https://matplotlib.org/) - Visualización de datos
- [Python](https://www.python.org/) - Lenguaje de programación

## 📊 Ejemplos de visualizaciones

### Vista principal
La vista principal muestra un gráfico de barras con los 20 mejores jugadores según su puntuación general.

### Vista de cláusulas
La vista alternativa muestra los 15 jugadores con las cláusulas de rescisión más altas.

## 📝 Requisitos

Ver el archivo `requirements.txt` para la lista completa de dependencias.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir lo que te gustaría cambiar o añadir.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.


---

Desarrollado con ❤️ por [Tu Nombre]
