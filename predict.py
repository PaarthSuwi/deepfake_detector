import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('model/deepfake_model.h5')

def predict_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)[0][0]
    return prediction > 0.5, prediction  # (True = Deepfake, confidence)
