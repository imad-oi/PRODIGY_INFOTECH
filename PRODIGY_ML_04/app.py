import streamlit as st
import cv2
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('hand_gesture_model.keras')

# Function to preprocess image for model prediction
def preprocess_image(image):
    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Resize image to match model input shape
    resized_image = cv2.resize(grayscale_image, (640, 240))
    print("Resized image shape:", resized_image.shape)
    # Normalize pixel values
    normalized_image = resized_image / 255.0
    # Reshape image to match model input shape
    processed_image = normalized_image.reshape((1, 240, 640))
    return processed_image

# Streamlit UI
st.title('Hand Gesture Recognition')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# Class labels
class_labels = ['palm', 'L', 'fist', 'fist_moved', 'thumb']

if uploaded_file is not None:
    # Read image file
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess image for model prediction
    processed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(processed_image)

    # Get predicted class
    predicted_class = np.argmax(prediction)

    # Display predicted class
    st.write('Predicted Class:', predicted_class)
