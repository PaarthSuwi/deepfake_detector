import cv2
import numpy as np
from tensorflow.keras.applications.xception import preprocess_input

def load_and_preprocess_image(image_path, target_size=(299, 299)):
    """
    Loads an image from disk, resizes it, and prepares it for model inference.
    
    Args:
        image_path (str): Path to the input image.
        target_size (tuple): Desired size for the model (default: 299x299 for Xception).

    Returns:
        np.ndarray: Preprocessed image ready for prediction.
    """
    try:
        # Load image
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize
        image = cv2.resize(image, target_size)

        # Normalize and preprocess
        image = image.astype("float32")
        image = preprocess_input(image)

        # Add batch dimension
        image = np.expand_dims(image, axis=0)
        return image

    except Exception as e:
        print(f"[ERROR] Could not preprocess image: {e}")
        return None
