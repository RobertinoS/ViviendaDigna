{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Rober\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\openpyxl\\styles\\stylesheet.py:226: UserWarning: Workbook contains no default style, apply openpyxl's default\n",
      "  warn(\"Workbook contains no default style, apply openpyxl's default\")\n",
      "2024-03-05 22:54:06.153 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Rober\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "Cannot subset columns with a tuple with more than one element. Use a list instead.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 28\u001b[0m\n\u001b[0;32m     25\u001b[0m     crear_graficas(df)\n\u001b[0;32m     27\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m---> 28\u001b[0m     \u001b[43mmain\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[1;32mIn[1], line 25\u001b[0m, in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m     22\u001b[0m st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mDashboard de Contabilidad\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     24\u001b[0m \u001b[38;5;66;03m# Mostrar las gráficas\u001b[39;00m\n\u001b[1;32m---> 25\u001b[0m \u001b[43mcrear_graficas\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdf\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[1;32mIn[1], line 13\u001b[0m, in \u001b[0;36mcrear_graficas\u001b[1;34m(df)\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcrear_graficas\u001b[39m(df):\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;66;03m# Crear gráficas utilizando los datos cargados\u001b[39;00m\n\u001b[0;32m     12\u001b[0m     fig, ax \u001b[38;5;241m=\u001b[39m plt\u001b[38;5;241m.\u001b[39msubplots()\n\u001b[1;32m---> 13\u001b[0m     \u001b[43mdf\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgroupby\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mCuenta\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mImp. presupuestado\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mImp. real\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[38;5;241m.\u001b[39msum()\u001b[38;5;241m.\u001b[39mplot(kind\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mbar\u001b[39m\u001b[38;5;124m'\u001b[39m, ax\u001b[38;5;241m=\u001b[39max)\n\u001b[0;32m     14\u001b[0m     plt\u001b[38;5;241m.\u001b[39mxticks(rotation\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m45\u001b[39m)\n\u001b[0;32m     15\u001b[0m     st\u001b[38;5;241m.\u001b[39mpyplot(fig)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\pandas\\core\\groupby\\generic.py:1957\u001b[0m, in \u001b[0;36mDataFrameGroupBy.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   1953\u001b[0m \u001b[38;5;66;03m# per GH 23566\u001b[39;00m\n\u001b[0;32m   1954\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(key, \u001b[38;5;28mtuple\u001b[39m) \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(key) \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m1\u001b[39m:\n\u001b[0;32m   1955\u001b[0m     \u001b[38;5;66;03m# if len == 1, then it becomes a SeriesGroupBy and this is actually\u001b[39;00m\n\u001b[0;32m   1956\u001b[0m     \u001b[38;5;66;03m# valid syntax, so don't raise\u001b[39;00m\n\u001b[1;32m-> 1957\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m   1958\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot subset columns with a tuple with more than one element. \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1959\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mUse a list instead.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1960\u001b[0m     )\n\u001b[0;32m   1961\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28msuper\u001b[39m()\u001b[38;5;241m.\u001b[39m\u001b[38;5;21m__getitem__\u001b[39m(key)\n",
      "\u001b[1;31mValueError\u001b[0m: Cannot subset columns with a tuple with more than one element. Use a list instead."
     ]
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "def cargar_datos():\n",
    "    # Cargar los datos desde un archivo CSV o cualquier otra fuente de datos\n",
    "    df = pd.read_excel('Reporte (3).xlsx')\n",
    "    return df\n",
    "\n",
    "def crear_graficas(df):\n",
    "    # Crear gráficas utilizando los datos cargados\n",
    "    fig, ax = plt.subplots()\n",
    "    df.groupby('Cuenta')['Imp. presupuestado', 'Imp. real'].sum().plot(kind='bar', ax=ax)\n",
    "    plt.xticks(rotation=45)\n",
    "    st.pyplot(fig)\n",
    "\n",
    "def main():\n",
    "    # Cargar los datos\n",
    "    df = cargar_datos()\n",
    "\n",
    "    # Crear el dashboard\n",
    "    st.title('Dashboard de Contabilidad')\n",
    "\n",
    "    # Mostrar las gráficas\n",
    "    crear_graficas(df)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
