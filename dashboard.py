import streamlit as st
import pandas as pd
import plotly.express as px


def presentacion():
    st.title('Bienvenidos a mi API para el Proyecto Individual Nº1 del Bootcamp Henry (Data Science)')
    st.write("Mi nombre es Robertino Garcia, alumno de Henry perteneciente al Cohorte Nº 17 (Full-Time)")
    st.write("[Link FastAPI Steam (/docs)](https://pi-ml-steam1.onrender.com/docs)")
    st.write("[Link del repositorio de GitHub](https://github.com/RobertinoS/PI_ML_OPS-Steam)")
    st.write("[Mi perfil de Linkedin](https://www.linkedin.com/in/robertino-pablo-garc%C3%ADa-sanguedolce-aa9306229/)")

presentacion()


# Cargar los datos
data = pd.read_excel('Reporte.xlsx')

# Crear nuevas columnas para categorizar las cuentas
data['Categoria'] = 'Otros'
data.loc[data['Cuenta'].str.contains('Sueldos|Cargas|Honorario|Beneficio|Indumenta'), 'Categoria'] = 'Gastos en Personal'
data.loc[data['Cuenta'].str.contains('Puntuales|Socios|Muni|Ingresos|Interes|Cobranza|Prestamo|Voluntar|Recupero'), 'Categoria'] = 'Ingresos'

# Crear un título para el dashboard
st.title("Dashboard de la Empresa")

# Mostrar los datos en una tabla
st.subheader("Vivienda Digna")
st.write(data)

# Gráfico interactivo de pastel para la categoría Gastos en Personal
#st.subheader("Gastos en Personal")
gastos_personal_counts = data[data['Categoria'] == 'Gastos en Personal']['Cuenta'].value_counts()
fig_gastos_personal = px.pie(values=gastos_personal_counts, names=gastos_personal_counts.index, title="Gastos en Personal")
st.plotly_chart(fig_gastos_personal, use_container_width=True)

# Gráfico interactivo de pastel para la categoría Ingresos
#st.subheader("Ingresos")
ingresos_counts = data[data['Categoria'] == 'Ingresos']['Cuenta'].value_counts()
fig_ingresos = px.pie(values=ingresos_counts, names=ingresos_counts.index, title="Ingresos")
st.plotly_chart(fig_ingresos, use_container_width=True)

# Gráficos interactivos de barras para Imp. presupuestado, Imp. real y Desvio
st.subheader("Imp. Presupuestado, Imp. Real, Desvio")
selected_column = st.selectbox("Seleccione una columna:", options=['Imp. presupuestado', 'Imp. real', 'Desvio'])
fig_bar = px.bar(data, x='Cuenta', y=selected_column, title=f"{selected_column} por Cuenta", width=800, height=500)
st.plotly_chart(fig_bar, use_container_width=True)
