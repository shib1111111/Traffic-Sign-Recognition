import streamlit as st
from PIL import Image
from functions import load_trained_model, predict_label
from signature import display_signature

# Page setup
st.set_page_config(
    page_title="Traffic Sign Recognition",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Title
st.title('Traffic Sign Recognition')


# Loading model
with st.spinner('Loading model...'):
    model = load_trained_model()

# Model loading error handling
if model is None:
    st.warning("Failed to load the model. Please ensure that the model file is correct and try again.")

# File uploader
uploaded_file = st.file_uploader("Upload an image (JPEG, JPG, PNG)", type=["jpg", "jpeg", "png"])

# Image analysis
if uploaded_file is not None:
    try:
        with st.spinner('Analyzing image...'):
            image = Image.open(uploaded_file)
            label = predict_label(image, model)
            if label is not None:
                st.image(image, caption='Uploaded Image', use_column_width=500)
                st.markdown(f'<style> .predicted-label {{ font-size: 25px; font-weight: bold; color: Yellow; }} </style>', unsafe_allow_html=True)
                st.write(f'<span><p>Predicted label:</p><p class="predicted-label">{label}</p></span>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display signature
display_signature()
