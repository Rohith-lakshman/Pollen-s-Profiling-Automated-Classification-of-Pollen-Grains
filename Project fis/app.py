from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import pickle
import os

# Load model and label classes
MODEL_PATH = "best_model.keras"
LABELS_PATH = "label_classes.pkl"

model = load_model(MODEL_PATH)
with open(LABELS_PATH, "rb") as f:
    class_names = pickle.load(f)

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part"

    file = request.files['image']
    if file.filename == '':
        return "No selected file"

    if file:
        file_path = os.path.join("static", file.filename)
        file.save(file_path)

        img = load_img(file_path, target_size=(128, 128))
        img = img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        class_index = np.argmax(prediction)
        class_name = class_names[class_index]
        confidence = float(np.max(prediction))

        return render_template('prediction.html',
                               image_path=file_path,
                               predicted=class_name,
                               confidence=confidence)

# Logout route
@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
