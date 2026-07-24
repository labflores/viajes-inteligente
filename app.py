import streamlit as st

# ----------------------------------------------------
# Configuración de la página
# ----------------------------------------------------
st.set_page_config(
    page_title="Viajes Inteligentes",
    page_icon="✨✈️✨",
    layout="centered"
)

# ----------------------------------------------------
# Título y descripción
# ----------------------------------------------------
st.title("Viajes Inteligentes✈️")

st.write(
    """
    Encontrá oportunidades de viaje según tu presupuesto 
    y tiempo disponible.
    """
)
#-----------------------------------------------------
# Búsqueda
#-----------------------------------------------------
with st.form("busqueda"):

    origen = st.text_input("Ciudad de origen")

    destino = st.text_input("Destino")

    fecha_inicio = st.date_input("Fecha de salida")

    fecha_fin = st.date_input("Fecha de regreso")

    presupuesto = st.number_input(
        "Presupuesto máximo",
        min_value=0
    )

    buscar = st.form_submit_button("Buscar oportunidad")

#------------------------------------------------------
if buscar:

    if origen == "" or destino == "":
        st.error("Completá origen y destino.")

    elif fecha_fin < fecha_inicio:
        st.error("La fecha de regreso no puede ser anterior.")

    else:

        with st.container():

            st.success("Búsqueda realizada")

            st.subheader("Resumen")

            st.write(f"**Origen:** {origen}")

            st.write(f"**Destino:** {destino}")

            st.write(f"**Presupuesto:** USD {presupuesto}")

#Resultado

            post = f"""
✈️ {destino.upper()}

🔥 Oferta encontrada

📅 {fecha_inicio:%d/%m/%Y}

💰 Desde USD {presupuesto}

🌎  ¡Animate! ✨
"""

            st.info(post)

#--------------------------------------------------
#Funciones
# -----------------------------------------------
def mostrar_post_instagram(destino, fecha, presupuesto):

    return f"""
✈️ {destino.upper()}

Vuelos encontrados

📅 {fecha:%d/%m/%Y}

💰 Desde $ {presupuesto}

🌎 ¡Animate a viajar! ✨
"""

st.info(
    mostrar_post_instagram(
        destino,
        fecha_inicio,
        presupuesto
    )
)








