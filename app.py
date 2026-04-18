import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv('pizzas.csv')

modelo = LinearRegression()
x = df[['diametro']]
y = df[['preço']]

modelo.fit(x,y)

st.title('Prevendo o valor de uma pizza')
st.divider()

diametro= st.number_input('Digite o tamanho da pizza:')

if diametro:
    preço_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'O valor da pizza com diâmetro de {diametro} cm é de R$ {preço_previsto:.2f}')
    st.balloons()
