import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

mobilenet_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)




def preprocess_image(img, target_size=(224, 224)):
    img = cv2.resize(img, target_size)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img



def analyze_leaf_image(image_path):
    full_path = os.path.join(BASE_DIR, image_path)

    img = cv2.imread(full_path)
    if img is None:
        return {"error": "Image not found"}

    processed_img = preprocess_image(img)

    features = mobilenet_model.predict(processed_img)

    return {
        "status": "Features extracted successfully",
        "feature_shape": features.shape
    }

