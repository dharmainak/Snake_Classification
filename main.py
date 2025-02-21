
import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

# Load the trained model
model = load_model('./Snake_Classification.keras')

st.title("🐍 Snake Classification App")

# Section: Choose a preset image or upload your own
st.subheader("Choose a preset image or upload your own")

# Preset images (Add your own image paths here)
preset_images = {
    "Venomous Snake 1": "./01AS-N8UP.jpg",
    "Venomous Snake 2":"./1_010.jpg",
    "Non-Venomous Snake 1": "./0e07f0ba188cf87784d3c48f54e91ce3.jpg"
}

# Select preset image
preset_choice = st.selectbox("Select a preset snake image:", ["None"] + list(preset_images.keys()))

# Upload image
uploaded_file = st.file_uploader("Or upload a snake image...", type=["jpg", "png", "jpeg"])

# Display selected or uploaded image
image_path = None  # Stores the final image path for processing


import os

# Initialize temp_file_path at the beginning to avoid NameError
temp_file_path = ""

if preset_choice != "None":
    image_path = preset_images[preset_choice]
    st.image(image_path, caption=f"Preset Image: {preset_choice}", use_column_width=True)

elif uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Define temp_file_path and save uploaded image
    temp_file_path = "temp_uploaded_image.jpg"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.read())

    image_path = temp_file_path  # Assign image path

# ✅ Prevents NameError when checking the file existence
if temp_file_path and os.path.exists(temp_file_path):
    st.write("Temporary file exists:", temp_file_path)

# Function to preprocess the image
def preprocess_image(image_path):
    img = load_img(image_path, target_size=(224, 224))  # Resize to match model input
    img = img_to_array(img) / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Predict if an image is selected or uploaded
if image_path:
    # Convert image to array
    image_array = preprocess_image(image_path)

    # Make prediction
    prediction = model.predict(image_array)

    # Interpret results
    class_names = ["Non-Venomous", "Venomous"]
    predicted_class = class_names[np.argmax(prediction)]

    st.write(f"### 🐍 Predicted Class: **{predicted_class}**")

    # Clean up temporary uploaded image
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
