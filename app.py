import streamlit as st
import PIL
from PIL import Image
from ultralytics import YOLO
import matplotlib.pyplot as plt

st.title('🌑 Rockfall Detection on Moon ')
st.markdown('#')
@st.cache_resource
def load_model():
# loading the model
    # Paste Model link here...
    model =  YOLO("best.pt")
    return model


def model_prediction(input_img,model):
    
    predicted = model.predict(input_img,save=True)
    for i, r in enumerate(predicted):
        # Plot results image
        print(i)
        im_bgr = r.plot()  # BGR-order numpy array
        im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image
        w,h = (im_rgb.size)
        if h<500:
            im_rgb = im_rgb.resize((w+200,h+100))
    return im_rgb


col1, col2 = st.columns(2,gap="medium")

with col1:
    st.header("Input")
    st.image("Input.tif")

with col2:
    st.header("Prediction")
    st.image("Output.tif")


st.divider()
st.write("""
         
### 📷 Choose Images from Below: 
""")



tab1, tab2, tab3 = st.tabs(["Image 1", "Image 2", "Image 3"])

with tab1:
   st.image("IMG1.tif",)

with tab2:
   st.image("IMG2.tif",width=600)

with tab3:
   st.image("IMG3.tif",)
st.write()
selected_image = st.selectbox("Select an image", ["IMG1.tif","IMG2.tif", "IMG3.tif"])

model = load_model()
if selected_image in ["IMG1.tif","IMG2.tif","IMG3.tif"]:
    input_imgs = Image.open(selected_image)
    predicted= model_prediction(input_imgs,model)
    st.divider()
    st.header("RockFalls Detected : ")
    st.image(predicted)

st.divider()

st.write("## Made by Shrirang Kanade 😎")


    