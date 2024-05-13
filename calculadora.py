import streamlit as st

def conversor():
    st.title('Conversor de Temperatura')

temperatura = st.number_input('Digite a temperaura: ')
medida = st.selectbox('Selecione a medida:',['Celsius (C)', 'Fahrenheit (F)', 'Kelvin (K)'])
st.write('|')
medida2 = st.selectbox('Selecione para qual medida deseja converter:',['Celsius (C)', 'Farenheit (C)', 'Kelvin (K)'])

if st.button('Converter'):
    if medida == 'Celsius (C)' and medida2 == 'Farenheit (F)':
        conversão = (temperatura * 1.8) + 32
    elif medida == 'Celsius (C)' and medida2 == 'Kelvin (K)':
        conversão = temperatura + 273
    elif medida == 'Fahrenheit (F)' and medida2 == 'Celsius (C)':
        conversão = (temperatura - 32) / 1.8
    elif medida == 'Fahrenheit (F)' and medida2 == 'Kelvin (K)':
        conversão = (temperatura + 459) * 5 / 9
    elif medida == 'Kelvin (K)' and medida2 == 'Celsius (C)':
        conversão = temperatura - 273
    elif medida == 'Kelvin (K)' and medida2 == 'Fahrenheit (F)':
        conversão = (temperatura - 273) * 9 / 5 + 32

    st.write('Resultado: ', conversão)

