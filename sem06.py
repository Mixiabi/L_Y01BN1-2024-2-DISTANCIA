import streamlit as st
import streamlit.components.v1 as components

st.subheader("Ejercicio 1: Imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")
        
st.subheader("Ejercicio 2: Imprimir los primeros 10 numeros")
if st.button("Ejecutar Ejercicio 2"):
    for i in range(1,11):
        st.write(i)
        
st.subheader("Ejercicio 3: Imprimir 'Hola Mundo' 10 veces")
num = st.number_input("Ingrese un numero para ver su tabla de mulitplicar del 1 al 12", min_value=1)

if st.button("Ejecutar Ejercicio 3"):
    for i in range(1,13):
        st.write(f'{num} * {i} = {num * i}')

#? *************************************************************************************
#?                              E J E R C I C I O   # 4
#? *************************************************************************************
if 'lista_numeros' not in st.session_state:
    st.session_state.lista_numeros = []

def set_autofocus():
    autofocus_script = """
    <script>
    document.getElementById("num_input").focus();
    </script>
    """
    components.html(autofocus_script)

def set_reinicio():
    if st.button("Reiniciar"):
        st.session_state.lista_numeros = []
        set_autofocus()

def set_calculo():
    media = sum(st.session_state.lista_numeros) / len(st.session_state.lista_numeros)
        
    mayores = len([num for num in st.session_state.lista_numeros if num > 10])
    iguales = len([num for num in st.session_state.lista_numeros if num == 10])
    menores = len([num for num in st.session_state.lista_numeros if num < 10])
        
    st.write(f"La media es: {media}")
    st.write(f"Mayores que 10: {mayores}")
    st.write(f"Iguales a 10: {iguales}")
    st.write(f"Menores que 10: {menores}")

# CSS personalizado para ajustar márgenes
st.markdown("""
    <style>
    .stTextInput > div {
        margin-bottom: 0px;
    }
    .stButton {
        margin-top: -10px;
    }
    </style>
""", unsafe_allow_html=True)

with st.form(key='my_form', clear_on_submit=True):
    numero = st.text_input("Ingresa un número y presiona Enter", key="num_input")
    submitted = st.form_submit_button("Agregar")
    set_autofocus()

if submitted and numero:
    
    if len(st.session_state.lista_numeros) < 10:
        st.write(f"Números ingresados: {st.session_state.lista_numeros}")
        try:
            numero = int(numero)
            st.session_state.lista_numeros.append(numero)
            set_calculo()
            
        except ValueError:
            st.write("Por favor, ingresa un número válido.")
        
            
    else:
        st.write("Ya has ingresado 10 números, no puedes agregar más.")
        st.write(f"Números ingresados: {st.session_state.lista_numeros}")

set_reinicio()