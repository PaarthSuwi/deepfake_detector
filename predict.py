import cv2
import numpy as np
from tensorflow.keras.models import load_model

from utils.preprocessing import load_and_preprocess_image

def predict_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)[0][0]
    return prediction > 0.5, prediction  # (True = Deepfake, confidence)

image = load_and_preprocess_image("path/to/image.png")
if image is not None:
    prediction = model.predict(image)

model = load_model('model/deepfake_model.h5')
