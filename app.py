import streamlit as st
from PIL import Image
import numpy as np
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="Plano a 3D",
    page_icon="📐",
    layout="wide"
)

st.title("📐 Conversor de Plano a 3D")
st.write("Sube una imagen de un plano para visualizar una representación 3D básica.")

# Cargar imagen
archivo = st.file_uploader(
    "Selecciona una imagen",
    type=["png", "jpg", "jpeg"]
)

if archivo is not None:

    # Mostrar imagen
    imagen = Image.open(archivo)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Plano cargado")
        st.image(imagen, use_container_width=True)

    with col2:

        st.subheader("Vista 3D")

        # Altura del modelo
        altura = st.slider(
            "Altura de extrusión",
            min_value=10,
            max_value=200,
            value=50
        )

        # Dimensiones de ejemplo
        largo = 100
        ancho = 60

        # Base
        x = [0, largo, largo, 0, 0]
        y = [0, 0, ancho, ancho, 0]

        fig = go.Figure()

        # Cara inferior
        fig.add_trace(
            go.Scatter3d(
                x=x,
                y=y,
                z=[0] * 5,
                mode="lines",
                name="Base"
            )
        )

        # Cara superior
        fig.add_trace(
            go.Scatter3d(
                x=x,
                y=y,
                z=[altura] * 5,
                mode="lines",
                name="Superior"
            )
        )

        # Aristas verticales
        for i in range(4):
            fig.add_trace(
                go.Scatter3d(
                    x=[x[i], x[i]],
                    y=[y[i], y[i]],
                    z=[0, altura],
                    mode="lines",
                    showlegend=False
                )
            )

        fig.update_layout(
            height=600,
            scene=dict(
                xaxis_title="X",
                yaxis_title="Y",
                zaxis_title="Z"
            ),
            margin=dict(l=0, r=0, b=0, t=0)
        )

        st.plotly_chart(fig, use_container_width=True)

    st.success("Modelo 3D generado correctamente.")
else:
    st.info("Sube una imagen para comenzar.")
