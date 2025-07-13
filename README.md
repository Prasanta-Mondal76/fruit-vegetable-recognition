# Fruit & Vegetable Recognition and Calorie Estimator 🍎🥦

## Overview
This AI-powered Streamlit web app identifies fruits or vegetables from an uploaded image and fetches their calorie information using the **Nutritionix API**. It uses a **fine-tuned MobileNetV2 deep learning model** trained on 36 food classes.


## How it Works
- Upload an image (JPG/PNG) of a fruit or vegetable.
- The app uses a MobileNetV2 model to identify the item.
- It then fetches the estimated calorie information using the Nutritionix API.
- Results are shown instantly on a web interface.

## 🧠 Dataset Description

The dataset includes images of **36 different fruits and vegetables**, organized by class folders.

### 🍎 Fruits:
Banana, Apple, Pear, Grapes, Orange, Kiwi, Watermelon, Pomegranate, Pineapple, Mango

### 🥦 Vegetables:
Cucumber, Carrot, Capsicum, Onion, Potato, Lemon, Tomato, Radish, Beetroot, Cabbage, Lettuce, Spinach, Soybean, Cauliflower, Bell Pepper, Chilli Pepper, Turnip, Corn, Sweetcorn, Sweet Potato, Paprika, Jalapeño, Ginger, Garlic, Peas, Eggplant

All images are resized to `224x224` during training.

## Files Included
- `Fruits_Vegetable_Classification.py` – Main Streamlit app
- `FV.h5` – Trained fruit & Vegetable classification model
- `mobilenet_v2_weights...h5` – MobileNetV2 base model weights
- `requirements.txt` – Required packages

## Requirements
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Create an API key in the Nutritionix API (required for calorie estimation).

3. Replace the code in `Fruits_Vegetable_Classification.py` under the function `fetch_calories(prediction)` with your `app_id` and `api_key`:
```python
app_id = "your_app_id"
api_key = "your_api_key"
```

## How to Run
1. Install Python 3.10.0 (Version must support TensorFlow)
2. Open terminal in the project folder.
3. Run:
   ```
   pip install -r requirements.txt
   ```
   After completing the installation, run 
   ```
   streamlit run Fruits_Vegetable_Classification.py
   ```
5. Use the browser link shown in the terminal (http://localhost:8501)

## Output
![Alt text](https://github.com/Prasanta-Mondal76/fruit-vegetable-recognition/blob/main/Screenshot.png)

## Credits
This project was developed as a practical demonstration of how AI and ML can be used in food recognition and calorie estimation.
Thanks to:

* `TensorFlow & Keras`
* `Streamlit`
* `Nutritionix API`

## Web App Link
`https://fruit-vegetable-recognition-nq79quf8t29ebwtglkbqmg.streamlit.app/`


### Note: This model is trained on 36 fruit and vegetable classes, with 100 images per class. Due to the limited dataset size, the model might sometimes misclassify or return "Unknown" even if the uploaded image belongs to one of the trained classes. This is expected behavior and can be improved by training the model on a larger and more diverse dataset.
