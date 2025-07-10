# Fruit & Vegetable Recognition and Calorie Estimator 🍎🥦

## Overview
This AI-powered Streamlit web app identifies fruits or vegetables from an uploaded image and fetches their calorie information using the Nutritionix API.

## How it Works
- Upload an image (JPG/PNG) of a fruit or vegetable.
- The app uses a MobileNetV2 model to identify the item.
- Then, it fetches the estimated calories using Nutritionix API.
- Results are shown instantly on a web interface.

## How to Run
1. Install Python 3.10 .
2. Open terminal in the project folder.
3. Run:
   ```
   pip install -r requirements.txt
   streamlit run Fruits_Vegetable_Classification.py
   ```
4. Use the browser link shown in terminal (http://localhost:8501)

## Requirements
Install dependencies:
```
pip install -r requirements.txt
```

## Files Included
- `Fruits_Vegetable_Classification.py` – Main Streamlit app
- `FV.h5` – Trained fruit & vegetable classification model
- `mobilenet_v2_weights...h5` – MobileNetV2 base model weights
- `requirements.txt` – Required packages


## Credits
Developed by Prasanta Mondal — as a practical demonstration of AI in food classification and calorie estimation.
