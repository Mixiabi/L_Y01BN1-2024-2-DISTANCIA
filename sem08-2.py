import re
import select
from unittest.runner import _ResultClassType
import streamlit as st

def calcular (operacion,num1,num2):
    """
    Realiza la operacion
    especificadad entre num1 y num2
    """
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Por favor, ingrese numero valido"
    if operacion == "Suma":
        return num1 + num2
    elif operacion == "Resta":
        return num1 - num2
    elif operacion == "Multiplicacion":
        return num1 * num2
    elif operacion == "Division":
        if num2 == 0:
            return "Error: no se puede dividir entre cero"
        return num1/num2
    else:
        return "Operacion no valida"
def main():
    st.title('calculadora basica')
    st.write('selecciones una operacion e ingrese los numeros')
    operacionLista = ['Suma','Resta','Multiplicacion','Division']
    operacion = st.selectbox(operacionLista)
    
    #? ENTRADAS PARA NUMERO
    num1 = st.text_input('Numero 1')
    num2 = st.text_input('numero 2')
    if st.button('calcular'):
        resultado = calcular(operacion, num1,num2)
        st.write('**Resultado:**',resultado)
if __name__ == "__main__":
    main()