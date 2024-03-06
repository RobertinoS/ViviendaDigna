import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
data = pd.read_excel(r'C:\Users\Rober\Desktop\Vivienda Digna\Reporte (3).xlsx')

# Crear nuevas columnas para categorizar las cuentas
data['Categoria'] = 'Otros'
data.loc[data['Cuenta'].str.contains('Sueldos|Cargas|Honorario|Beneficio|Indumenta'), 'Categoria'] = 'Gastos en Personal'
data.loc[data['Cuenta'].str.contains('Puntuales|Socios|Muni|Ingresos|Interes|Cobranza|Prestamo|Voluntar|Recupero'), 'Categoria'] = 'Ingresos'

# Crear un título para el dashboard
st.title("Dashboard de la Empresa")

# Mostrar los datos en una tabla
st.subheader("Datos de la Empresa")
st.write(data)

# Gráfico interactivo de pastel para la categoría Gastos en Personal
st.subheader("Diagrama de Pastel: Gastos en Personal")
gastos_personal_counts = data[data['Categoria'] == 'Gastos en Personal']['Cuenta'].value_counts()
fig_gastos_personal = px.pie(values=gastos_personal_counts, names=gastos_personal_counts.index, title="Gastos en Personal")
st.plotly_chart(fig_gastos_personal, use_container_width=True)

# Gráfico interactivo de pastel para la categoría Ingresos
st.subheader("Diagrama de Pastel: Ingresos")
ingresos_counts = data[data['Categoria'] == 'Ingresos']['Cuenta'].value_counts()
fig_ingresos = px.pie(values=ingresos_counts, names=ingresos_counts.index, title="Ingresos")
st.plotly_chart(fig_ingresos, use_container_width=True)

# Gráficos interactivos de barras para Imp. presupuestado, Imp. real y Desvio
st.subheader("Gráficos de Barras: Imp. Presupuestado, Imp. Real, Desvio")
selected_column = st.selectbox("Seleccione una columna:", options=['Imp. presupuestado', 'Imp. real', 'Desvio'])
fig_bar = px.bar(data, x='Cuenta', y=selected_column, title=f"{selected_column} por Cuenta", width=800, height=500)
st.plotly_chart(fig_bar, use_container_width=True)
