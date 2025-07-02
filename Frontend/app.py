import streamlit as st
import requests
from loguru import logger

API_URL = 'http://localhost:8000/calcul'

st.title('Calcul du carré d\'un entier')
# n = st.number_input('Entrez un entier', value=0, step=1)
# logger.debug(type(n))
# print(n)
# if st.button('Calculer'):
#     try:
#         response = requests.post(API_URL, json={'n': int(n)}, timeout=3)
#         response.raise_for_status()
#         result = response.json().get('result')
#         st.success(f'Le carré de {n} est {result}')
#         logger.info(f'Square computed: {n} → {result}')
#     except Exception as e:
#         st.error(f'Erreur: {e}')
#         logger.error(f'Error calling API: {e}')
     
with st.form(key="HIDING_FORM"):
    n = st.number_input('Entrez un entier', value=0, step=1)
    submit_button = st.form_submit_button(label='Calculer')
    if submit_button:
        pyload= {'n': int(n)}
        try:
            response = requests.post(API_URL, json=pyload, timeout=3)
            response.raise_for_status()
            result = response.json().get('result')
            st.success(f'Le carré de {n} est {result}')
            logger.info(f'Square computed: {n} → {result}')
        except Exception as e:
            st.error(f'Erreur: {e}')
            logger.error(f'Error calling API: {e}')
