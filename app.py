
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="León Trader Dashboard", layout="wide")

# Sidebar
st.sidebar.title("📊 León Trader Dashboard")
st.sidebar.info("Plataforma privada de seguimiento de rendimiento para traders.")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV de operaciones", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Fecha"])
    
    st.title("📈 Curva de Capital")
    fig = px.line(df, x="Fecha", y="Balance final", title="Evolución del Balance")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.title("📊 Estadísticas Generales")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Operaciones totales", len(df))
    with col2:
        st.metric("Ganancia total (USD)", round(df["Resultado (USD)"].sum(), 2))
    with col3:
        winrate = (df["Resultado (USD)"] > 0).mean() * 100
        st.metric("Winrate", f"{winrate:.2f}%")

    st.markdown("---")
    st.subheader("📂 Tabla de Operaciones")
    st.dataframe(df, use_container_width=True)
else:
    st.title("👋 Bienvenido al León Trader Dashboard")
    st.write("Por favor, sube tu archivo CSV de operaciones para comenzar.")
