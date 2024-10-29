from os import error
import streamlit as st

def validate_data(marca, modelo, kilometraje):
    if not marca or not modelo:
        return "La marca y modelo no deben estar vacio"
    try:
        kilometraje = float(kilometraje)
        if kilometraje < 0:
            return "el kilometraje no puede ser menor que 0"
    except ValueError:
        return "el kilometraje debe ser un numero valido"
    return None
    
def main():
    st.title("Registro de automovil")
    st.write("ingrese los datos del automovil")
    
    marca = st.text_input("marca del automovil")
    modelo = st.text_input("modelo")
    kilometraje = st.text_input("kilometraje")
    
    if st.button("registrar"):
        error = validate_data(marca,modelo,kilometraje)
        if error:
            st.error(error)
        else:
            st.success("automovil registrado exitosamente")
            st.write("**Marca:** ",marca)
            st.write("**Modelo:** ",modelo)
            st.write("**Kilometraje:** ",kilometraje)
            
if __name__ == "__main__":
    main()
#? solo si se ejecuta directamente y no desde otro archivo