import streamlit as st
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import requests
from bs4 import BeautifulSoup
import os

model = load_model('FV.h5')
labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot', 7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger', 14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
          19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple', 26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn', 32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}

fruits = ['Apple','Banana','Bello Pepper','Chilli Pepper','Grapes','Jalepeno','Kiwi','Lemon','Mango','Orange','Paprika','Pear','Pineapple','Pomegranate','Watermelon']
vegetables = ['Beetroot','Cabbage','Capsicum','Carrot','Cauliflower','Corn','Cucumber','Eggplant','Ginger','Lettuce','Onion','Peas','Potato','Raddish','Soy Beans','Spinach','Sweetcorn','Sweetpotato','Tomato','Turnip']

def fetch_calories(prediction):
    app_id = "670a87ff"
    api_key = "6a910d2d6ccc6448b43ff57e6273239f"
    
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": app_id,
        "x-app-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "query": prediction,
        "timezone": "US/Eastern"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        result = response.json()
        calories = result["foods"][0]["nf_calories"]
        return f"{int(calories)} kcal (per serving)"
    except Exception as e:
        print(e)
        return None

def processed_img(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    pred_index = np.argmax(prediction)

    confidence = np.max(prediction)

    # If model is not confident enough (< 0.85), return Unknown
    if confidence < 0.85:
        return "Unknown", "Unknown"

    predicted_label = labels[pred_index].capitalize()

    if predicted_label in vegetables:
        return predicted_label, "Vegetables"
    elif predicted_label in fruits:
        return predicted_label, "Fruits"
    else:
        return "Unknown", "Unknown"

def run():
    st.title("Fruits🍍-Vegetable🍅 Classification")
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])

    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_container_width=False)

        save_image_path = './upload_images/' + img_file.name

        if not os.path.exists('upload_images'):
            os.makedirs('upload_images')

        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        result, category = processed_img(save_image_path)

        if result == "Unknown":
            st.error("**Category : Unknown**")
            st.warning("⚠️ This item is not recognized from the 36 known classes.")
            st.info("Calories not available for unknown items.")
        else:
            st.info(f"**Category : {category}**")
            st.success(f"**Predicted : {result}**")

            cal = fetch_calories(result)
            if cal:
                st.warning('**' + cal + '(100 grams)**')
            else:
                st.info("Calories not found")


run()
