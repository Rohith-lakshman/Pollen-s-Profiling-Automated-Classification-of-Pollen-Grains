Project Execuctable files

# 🌿 Pollen's Profiling: Automated Classification of Pollen Grains

This project automates the classification of pollen grains using a Convolutional Neural Network (CNN) with a Flask-based web application interface.

---

## 📂 Project Structure

```
Pollen-Classifier/
│
├── app.py                         # Flask app to serve the trained CNN model
├── Pollen_gain_Classification.ipynb # Jupyter Notebook for EDA + model training
├── best_model.keras               # Trained CNN model
├── label_classes.pkl              # Pickled class label mappings
├── requirements.txt               # List of required Python packages
├── README.md                      # Project overview (this file)
│
├── archive (3)/                   # Dataset (unzip if compressed)
│   └── class_name_1.jpg           # Sample pollen images
│
├── static/                        # Optional static files (CSS/JS/images)
│
├── templates/                     # Flask HTML templates
│   ├── index.html                 # Upload interface
│   ├── prediction.html            # Result page
│   └── logout.html                # Logout/confirmation page
│
├── uploads/                       # Temporary uploaded image storage
```

---

## 💻 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Rohith-lakshman/Pollen-s-Profiling-Automated-Classification-of-Pollen-Grains/tree/main
cd Pollen-Classifier
```

Or download as ZIP and extract the folder.

---

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Linux/macOS
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Prepare the Dataset

* Ensure `archive (3)/` folder exists with image files like `hyptis_01.jpg`, `qualea_02.jpg`, etc.
* If zipped, unzip it inside the project root.

---

### 5. Train the Model 

Open the notebook:

```bash
jupyter notebook Pollen_gain_Classification.ipynb
```

This will:

* Load and preprocess images
* Train a CNN model
* Save:

  * `best_model.keras`
  * `label_classes.pkl`

---

### 6. Run the Flask Web Application

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

Upload a pollen image to get the predicted class and confidence.

---

## 🗂 File Path Notes

Make sure the following files are correctly placed:

* `best_model.keras` — root folder
* `label_classes.pkl` — root folder
* HTML files — inside `templates/`
* Upload folder — `uploads/` (can be empty but must exist)

---

## 🎨 Sample Test Images

Try using:

* `qualea_10.jpg`
* `croton_01.jpg`
* `serjania_03.jpg`

These must exist inside `archive (3)`
