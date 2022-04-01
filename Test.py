import cv2
import streamlit as st
import numpy as np
from PIL import Image
st.header("Object Counting using OpenCV")
st.write("Press Default buttom if you don't have image to count objects")
image_file = None
image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])


if st.button("Default"):
    original_image = Image.open("Downloads/object2.jpg")
    


else:
    original_image = Image.open(image_file)
    

original_image = np.array(original_image)

blurred = cv2.GaussianBlur(original_image,(11,11),0)

gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 225,225,cv2.THRESH_BINARY_INV)[1]

(counts,_) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = original_image.copy()
cv2.drawContours(contour, counts, -1,(255,0,0),3)

st.image([original_image, contour])
st.write("total obj = ", len(counts))