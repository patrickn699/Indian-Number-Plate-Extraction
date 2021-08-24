import streamlit as st
import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from utils import Load_model
from get_num_plate import get_number_plate
from get_details import fetch
#os.environ['KMP_DUPLICATE_LIB_OK']='True'

l = Load_model()
g = get_number_plate()
cfg = l.load_model()
#det = details()




#st.title('Indian Number Plate Detection')
st.markdown("<h1 style='text-align: center; color: black;'>India Number Plate Detection</h1>", unsafe_allow_html=True)
st.image('h2.jpg')
st.write(' ')
st.write(' ')
st.write(' ')

if st.checkbox('show/hide information'):
    st.info('This is the first release so there might be some wrong results')
    st.info('Please make sure you upload clean and image of the license plate')
    st.info('The uploaded image should not contain number plate which is far away')
    st.info('The uploaded image should not be  blured or distorted')
    st.info('You can click the below checkbox to see sample of images.')

if st.checkbox('Click to see sample images'):
    st.image(os.path.join('Images','4556.jpg'))
    st.image(os.path.join('Images','4558.jpg'))
    st.image(os.path.join('Images','45130.jpg'))

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

st.write('Please upload an image')
#up_img = st.file_uploader(label='',type = ['png','jpg'])
#img = Image.open(up_img)
#np_i = np.array(img)
#st.write(np_i)

try:
    up_img = st.file_uploader(label='',type = ['png','jpg'])
    st.image(up_img)
    op, img = l.predict(up_img, cfg)
    grap = l.visulize(img, cfg, op)
    st.image(grap)
    plts = g.run_easy_ocr(op, img)
    #st.image(grap)

    print(plts)
    st.write(plts)
    numbers = st.selectbox('Select the vehicile number you are looking for', list(plts))
    st.write(numbers)

    if numbers != None:
        st.success('Trying to fetch the details please wait...')
        data = fetch(numbers)
        st.dataframe(data)

    else:
        st.error('unable to fetch the details')

except Exception as e:
    #st.write(e)
    #st.warning('Image not uploaded')
    st.warning(e)


