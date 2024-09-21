import streamlit as st

#* inicializacion de variables
usuario = []

#* funcion agregar un usurario
def agregar_usuario(nombre):
    usuario.append(nombre)
    st.success(f"Usuario {usuario} agregado",icon="✅")

#* Mostrar usuarios
def mostrar_usuario():
    if usuario:
        st.write("Lista de usuarios")
        for usuario in usuario:
            st.write(f"- {usuario}")
    else:
        st.warning("No hay usuarios registrados")

#* Menu principal
st.title("Gestion de usuarios")

#* Opciones
opcion = st.selectbox("selecciona una opcion:" , ["Agregar usuarios","Mostrar usuarios"])
if opcion == "Agregar usuarios":
    nombre = st.text_input('nombre del usuario')
    if st.button("Agregar", type='primary'):
        if nombre:
            agregar_usuario(nombre)
        else:
            st.error("No puede estar vacio")
elif opcion == "Mostrar usuarios":
    mostrar_usuario ()
