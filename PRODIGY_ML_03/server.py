import streamlit as st
import cv2
import numpy as np
import pickle
from PIL import Image
from io import BytesIO
# Function to preprocess uploaded image
# def preprocess_image(image):
#     img = cv2.imread(image, 0)
#     img = cv2.resize(img, (50, 50))  # Resize image to a uniform size
#     img = img.flatten() / 255.0  # Normalize pixel values
#     return img

def preprocess_image(file):
    img = np.array(Image.open(BytesIO(file.read())))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Convert to grayscale
    img = cv2.resize(img, (50, 50))  # Resize image to a uniform size
    img = img.flatten() / 255.0  # Normalize pixel values
    return img

# Load the trained SVM model
with open('model.sav', 'rb') as file:
    svm_model = pickle.load(file)

# Streamlit app
def main():
    st.title('Dog vs Cat Classifier')

    # Upload image file
    uploaded_file = st.file_uploader("Upload an image of a dog or a cat", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
             # Display the uploaded image
            st.image(uploaded_file, caption='Uploaded Image',width=300,  use_column_width=False)

            image = preprocess_image(uploaded_file)
            prediction = svm_model.predict([image])

            if prediction[0] == 1:
                st.success("It's a dog!")
            else:
                st.success("It's a cat!")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
