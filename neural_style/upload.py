# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image
from streamlit import caching

import style


def upload_image():
    global image

    st.title('Style Transfer')

    image_file = st.file_uploader("Upload", type=["png", "jpg"])

    img = st.selectbox(
        'Select Image',
        ('amber.jpg', 'cat.png')
    )

    style_name = st.selectbox(
        'Select Style',
        ('candy', 'mosaic', 'rain_princess', 'udnie')
    )


    model= "saved_models/" + style_name + ".pth"
     
    output_image = "images/output-images/" + style_name + "-" + img

    if image_file is not None:
        print("Successfully Uploaded!!!")
        input_image = "images/content-images/" + img
        image = Image.open(image_file)
    else:
        input_image = "images/content-images/" + img
        image = Image.open(input_image)

    st.write('### Source image:')
    st.image(image, width=700) # image: numpy array

    clicked = st.button('Stylize')

    if clicked:
        caching.clear_cache()
        model = style.load_model(model)
        style.stylize(model, input_image, output_image)

        st.write('### Output image:')
        image = Image.open(output_image)
        st.image(image, width=700)
