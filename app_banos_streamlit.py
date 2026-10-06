import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title='Descubre Baños - Paúl Maldonado',
    page_icon='♨️️',
    layout='centered'
)

# Base de datos de la app
DATOS_BANOS = {
    'balnearios': [
        {
            'nombre': 'Hostería Durán / Balneario Termal',
            'tipo': 'Aguas Termales & Spa',
            'temp': '38°C - 41°C',
            'horario': '06:00 - 22:00',
            'precio': 6.0,
            'lat': -2.9189,
            'lon': -79.0625,
            'servicios': ['Piscinas termales', 'Turco', 'Hidromasaje', 'Restaurante'],
            'desc': 'El complejo termal tradicional más emblemático de Baños.'
        },
        {
            'nombre': 'Piedra de Agua Fuente Termal & Spa',
            'tipo': 'Spa Subterráneo & Termas',
            'temp': '36°C - 40°C',
            'horario': '08:00 - 21:00',
            'precio': 12.0,
            'lat': -2.9195,
            'lon': -79.0632,
            'servicios': ['Lodoterapia', 'Cueva subterránea', 'Masajes'],
            'desc': 'Spa de lujo con tratamientos de barro volcánico.'
        }
    ],
    'gastronomia': [
        {
            'nombre': 'Huecas del Parque Central',
            'plato': 'Empanadas de viento y morocho',
            'horario': '15:00 - 22:00',
            'lat': -2.9182,
            'lon': -79.0618,
            'desc': 'Empanadas gigantes y morocho caliente.'
        }
    ],
    'senderos': [
        {
            'nombre': 'Sendero Mirador El Calvario',
            'dificultad': 'Media-Baja',
            'duracion': '45 min',
            'lat': -2.9175,
            'lon': -79.06,
            'desc': 'Caminata hacia el mirador panorámico.'
        }
    ]
}

# --- BARRA LATERAL (BRANDING DE PAÚL MALDONADO) ---
st.sidebar.markdown("### 🏛️ Un proyecto de:")

# Mostrar logo e imagen en dos columnas
col_logo1, col_logo2 = st.sidebar.columns(2)
with col_logo1:
    st.image("https://img.icons8.com/color/96/hot-springs.png", width=70)
with col_logo2:
    # Ruta exacta de la imagen jpg en Descargas
    st.image("paul_maldonado.jpg", use_container_width=True)

st.sidebar.markdown("## **Paúl Maldonado**")
st.sidebar.markdown("### 🚀 *Renovando Baños*")
st.sidebar.divider()

# Navegación
st.sidebar.title('Navegación')
opcion = st.sidebar.radio(
    'Selecciona una sección:',
    ['🏠 Inicio', '🌊 Balnearios y Spas', '🍽️ Ruta Gastronómica', '🥾 Senderos y Miradores', '🗺️ Mapa General']
)

# --- ENCABEZADO PRINCIPAL DE LA APP ---
st.title('♨️ Descubre Baños')
st.caption('Guía Turística y Tecnológica | **Renovando Baños con Paúl Maldonado**')

# --- CONTENIDO DE LAS SECCIONES ---
if opcion == '🏠 Inicio':
    st.subheader('¡Bienvenido a Baños de Cuenca!')
    st.write("""
    Esta aplicación es un proyecto enfocado en la **reactivación económica, turística y digital** 
    de la parroquia Baños.
    """)
    st.success("✨ **Propuesta de Desarrollo:** Impulsada por **Paúl Maldonado** — *Renovando Baños*.")
    
    col1, col2 = st.columns(2)
    col1.metric('Temp. Agua Termal', '38 °C')
    col2.metric('Desde Cuenca', '15 min')

elif opcion == '🌊 Balnearios y Spas':
    st.subheader('🌊 Balnearios Termales')
    for b in DATOS_BANOS['balnearios']:
        with st.expander(f"📌 {b['nombre']}"):
            st.write(f"**Tipo:** {b['tipo']} | **Temp:** {b['temp']}")
            st.write(f"**Horario:** {b['horario']} | **Entrada:** ${b['precio']:.2f}")
            st.write(f"**Servicios:** {', '.join(b['servicios'])}")
            st.caption(b['desc'])

elif opcion == '🍽️ Ruta Gastronómica':
    st.subheader('🍽️ Huecas y Comida Típica')
    for g in DATOS_BANOS['gastronomia']:
        st.markdown(f"### 🥐 {g['nombre']}")
        st.write(f"**Especialidad:** {g['plato']}")
        st.write(f"**Horario:** {g['horario']}")
        st.caption(g['desc'])

elif opcion == '🥾 Senderos y Miradores':
    st.subheader('🥾 Ecoturismo y Senderismo')
    for s in DATOS_BANOS['senderos']:
        st.markdown(f"### 🏔️ {s['nombre']}")
        st.write(f"**Dificultad:** {s['dificultad']} | **Tiempo:** {s['duracion']}")
        st.caption(s['desc'])

elif opcion == '🗺️ Mapa General':
    st.subheader('🗺️ Mapa de Atractivos')
    puntos = (
        [{'lat': b['lat'], 'lon': b['lon']} for b in DATOS_BANOS['balnearios']] +
        [{'lat': g['lat'], 'lon': g['lon']} for g in DATOS_BANOS['gastronomia']] +
        [{'lat': s['lat'], 'lon': s['lon']} for s in DATOS_BANOS['senderos']]
    )
    st.map(puntos, zoom=14)