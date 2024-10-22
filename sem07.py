import streamlit as st
def mostrar_menu():
    st.title("ejemplo de menu")
    st.write("selecciona una opcion del menu")
    menu=["Archivo","Editar","Ver","Salir"]
    seleccion = ""
    seleccion = st.radio("Menu", menu)
    if seleccion == "Archivo":
        st.write("seleccionaste: archivo")
    elif seleccion == "Editar":
        st.write("seleccionaste: editar")
    elif seleccion == "Ver":
        st.write("seleccionaste: editar")
    elif seleccion == "Salir":
        st.write("Saliendo del menu")

if __name__ == "__main__":
    mostrar_menu()