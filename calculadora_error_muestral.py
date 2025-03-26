import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

# st.set_page_config(
#     page_title="Calculadora Margen de Error",
#     layout="wide"
# )

# st.title("Calculadora Margen de Error")

import streamlit as st
import streamlit as st

if not st.experimental_user.is_logged_in:
    st.login("google")
else:
    st.write(f"Hello, {st.experimental_user.name}!")

# def calcular_error_muestral(universo, casos, nivel_confianza=1.96, p=0.5):
#     """
#     Calcula el error muestral.
    
#     Args:
#         universo (float): Tamaño de la población
#         casos (float): Tamaño de la muestra
#         nivel_confianza (float): Valor Z (por defecto 1.96 para 95%)
#         p (float): Proporción esperada (por defecto 0.5)
    
#     Returns:
#         float: Error muestral en porcentaje
#     """
#     try:
#         if casos > universo:
#             return None
#         if casos == 0:
#             return None
            
#         q = 1 - p
#         error = nivel_confianza * np.sqrt((p * q) / casos) * np.sqrt((universo - casos) / (universo - 1))
#         return error * 100
#     except:
#         return None

# # # Configuración del nivel de confianza
# # nivel_confianza = st.selectbox(
# #     "Seleccione el nivel de confianza:",
# #     options=["90%", "95%", "99%"],
# #     index=1  # 95% por defecto
# # )

# # # Mapear el nivel de confianza al valor Z
# # z_values = {
# #     "90%": 1.645,
# #     "95%": 1.96,
# #     "99%": 2.576
# # }
# z_value = 1.96

# # Widget para subir archivo
# uploaded_file = st.file_uploader("Subir archivo Excel con columnas 'Poblacion' y 'Casos'", type=['xlsx'])

# if uploaded_file:
#     try:
#         # Leer el archivo
#         df = pd.read_excel(uploaded_file)
        
#         # Verificar que existan las columnas necesarias
#         required_columns = ['Poblacion', 'Casos']
#         if not all(col in df.columns for col in required_columns):
#             st.error("El archivo debe contener las columnas 'Poblacion' y 'Casos'")
#             st.stop()
        
#         # Calcular el error muestral para cada fila
#         df['Error_Muestral'] = df.apply(
#             lambda row: calcular_error_muestral(
#                 row['Poblacion'], 
#                 row['Casos'], 
#                 z_value
#             ),
#             axis=1
#         )
        
#         # Mostrar los resultados
#         st.write("### Resultados:")
#         st.dataframe(
#             df.style.format({
#                 'Margen_Error': '{:.2f}%'
#             }),
#             use_container_width=True,hide_index=True
#         )
        
#         # Botón para descargar resultados
#         buffer = BytesIO()
#         with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
#             df.to_excel(writer, index=False, sheet_name='Resultados')
#             # Ajustar el ancho de las columnas
#             worksheet = writer.sheets['Resultados']
#             for idx, col in enumerate(df.columns):
#                 worksheet.set_column(idx, idx, 15)
        
#         st.download_button(
#             label="📥 Descargar resultados",
#             data=buffer.getvalue(),
#             file_name="resultados_margen_error.xlsx",
#             mime="application/vnd.ms-excel"
#         )
        
#     except Exception as e:
#         st.error(f"Error al procesar el archivo: {str(e)}")
# else:
#     # Mostrar ejemplo del formato esperado
#     st.info("El archivo Excel debe tener el siguiente formato:")
#     ejemplo = pd.DataFrame({
#         'Poblacion': [1000000, 500000],
#         'Casos': [1000, 500]
#     })
#     st.dataframe(ejemplo,hide_index=True)
