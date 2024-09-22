import streamlit as st

mxi = """
<style>
header{
    color:yellow;
}
[data-testid="stHeader"]{
    background-color:#73c6b6
}
[data-testid="stApp"]{
    background-color:#cd7c7c;
}
[data-testid="stAppViewBlockContainer"]{
    background-color: #54658e;
}
[data-testid="stMarkdownContainer"]{
    color:#ffffff;
}
h1{
    color: #32CD32; /* Verde lima */
}
h2{
    color: #FFC300;
}
/*      B U T T O N        */
[data-testid="stBaseButton-primary"]{
    background-color: #9b0af9;
    color: white;
    border-radius: 12px;
    border: 2px solid #FF4500;
    padding: 10px 24px; /* Tam botón */
    font-size: 16px; /* Tam fuente */
    cursor: pointer; /* pasar por encima */
}
[data-testid="stBaseButton-secondary"]{
    background-color: #9b0af9;
    color: white;
    border-radius: 12px;
    border: 2px solid #FF4500;
    padding: 10px 24px; /* Tam botón */
    font-size: 16px; /* Tam fuente */
    cursor: pointer; /* pasar por encima */
}
[data-testid="stAlertContainer"]{
    background-color: #FF4500;
    color:blue;
}
.st-emotion-cache-1m1jr3q e1eexb540{
    
    cursor:ponter;
}
<style>
"""

st.markdown(mxi,unsafe_allow_html=True)

#* inicializacion de variables
if 'usuarios' not in st.session_state:
    st.session_state['usuarios']=[]

#* funcion agregar un usuario
def agregar_usuario(nombre):
    st.session_state['usuarios'].append(nombre)
    st.success(f"Usuario {nombre} agregado", icon="✅")

#* Mostrar usuarios
def mostrar_usuario():
    if st.session_state['usuarios']:  # Verificar si la lista tiene usuarios
        # st.write("Lista de usuarios:")
        for usuario in enumerate(st.session_state['usuarios']):  # Iterar sobre la lista de session_state
            st.write(f" {usuario} ")
    else:
        st.warning("No hay usuarios registrados")
        
#* Eliminar usuarios
def eliminar_usuario():
    if st.session_state['usuarios']:
        index = st.number_input("",min_value=0, max_value=len(st.session_state['usuarios'])-1, step=1)
        if st.button('Eliminar usuario'):
            eliminado = st.session_state['usuarios'].pop(index)  # Eliminar por índice
            st.success(f"Usuario {eliminado} eliminado", icon="🗑️")
    else:
        st.warning("No hay usuarios registrados para eliminar")
        

#* Menu principal
st.title("Gestión de usuarios")

#* Opciones
opcion = st.selectbox("Selecciona una opción:",("Agregar usuarios", "Mostrar usuarios","Eliminar usuario"))

if opcion == "Agregar usuarios": 
    st.header("Agregando usuario")
    nombres = st.text_input('Nombre del usuario')
    if st.button("Agregar", type='primary'):
        if nombres:
            agregar_usuario(nombres)
        else:
            st.error("Ingrese un nombre de usuario")
elif opcion == "Mostrar usuarios":
    
    if st.button("Mostrar usuarios", type="primary"):
        st.header("Lista de usuarios")
        mostrar_usuario()
elif opcion == "Eliminar usuario":
    st.header("Eliminado usuarios de la lista")
    eliminar_usuario()