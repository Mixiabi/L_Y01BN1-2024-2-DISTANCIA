import streamlit as st
def verificar_automoviles():
    st.title("Centro de verificacion de automoviles")
    
    #! Lista de puntos contaminantes
    if 'puntosContaminantes' not in st.session_state:
        st.session_state.puntosContaminantes = []
    puntos = st.number_input('ingrese los puntos pcontaminantes del automovil', min_value=0.0,step=0.1)
    
    #? Registar automovil
    if st.button('registrar automovil', type= 'primary'):
        st.session_state.puntosContaminantes.append(puntos)
        st.success(f'Automobvil registrado con {puntos} puntos contaminantes')
    
    #* Mostrar datos registrados
    if len(st.session_state.puntosContaminantes)>0 and st.button("calcular resultados"):
        promedio = sum(st.session_state.puntosContaminantes)/len(st.session_state.puntosContaminantes)
        menosContaminacion = min(st.session_state.puntosContaminantes)
        masContaminacion = max(st.session_state.puntosContaminantes)
        
        #! Mostrar resultado
        st.write(f'Promedio de puntos contaminantes {promedio:.2f}')
        st.write(f'El automovil que menos contamino {menosContaminacion:.2f}')
        st.write(f'El automovil que menos contamino {masContaminacion:.2f}')
    
    #*Opcion para reiniciar datos
    if st.button("reiniciar datos"):
        st.session_state.puntosContaminantes =[]    
        st.success('Datos reiniciados correctamente')

#?Ejecutar funcion
if __name__ == "__main__":
    verificar_automoviles()
        