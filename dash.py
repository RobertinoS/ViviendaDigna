import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
data = pd.read_excel(r'C:\Users\Rober\Desktop\Vivienda Digna\Reporte (3).xlsx')

# Crear un título para el dashboard
st.title("Dashboard de la Empresa")

# Mostrar los datos en una tabla
st.subheader("Datos de la Empresa")
st.write(data)

# Gráfico interactivo de pastel para la cantidad de cuentas
st.subheader("Diagrama de Pastel: Cantidad de Cuentas")
cuenta_counts = data['Cuenta'].value_counts()
fig = px.pie(values=cuenta_counts, names=cuenta_counts.index)
st.plotly_chart(fig)

# Gráficos interactivos de barras para Imp. presupuestado, Imp. real y Desvio
st.subheader("Gráficos de Barras: Imp. Presupuestado, Imp. Real, Desvio")
selected_column = st.selectbox("Seleccione una columna:", options=['Imp. presupuestado', 'Imp. real', 'Desvio'])
fig = px.bar(data, x=data.index, y=selected_column)
st.plotly_chart(fig)
