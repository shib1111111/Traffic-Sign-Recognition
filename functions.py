import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from labels import classes  

# Function to load the pre-trained model
@st.cache_resource()
def load_trained_model():
    try:
        model = load_model('./model/model.h5')
        model.load_weights("./model/model_weights")
        return model
    except Exception as e:
        st.error('Error loading model: {}'.format(str(e)))
        return None

# Preprocess the uploaded image
def preprocess_image(image):
    image = image.resize((30, 30))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Predict label for the uploaded image
def predict_label(image, model):
    try:
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        label = classes[np.argmax(prediction)]
        return label
    except Exception as e:
        st.error('Error predicting label: {}'.format(str(e)))
        return None
