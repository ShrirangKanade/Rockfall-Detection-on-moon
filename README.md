# Rockfall Detection on Moon using YoloV8 ✨

This repository represents a web app with a YoloV8 object detection model which detects rockfall on moon.


## 📄 Description
* This project is developed to solve the problem of detecting rockfall (eg. rocks) on lunar surface.

* Implementation is based on the ultralytics YOLOv8.

* In planetary science, the spatial distribution and frequency of rockfalls provide insights into the global erosional state and activity of a planetary body.
* Their tracks act as tools that allow for the remote estimation of the surface strength properties of yet unexplored regions in preparation of future ground exploration missions.

## 📁 Dataset 

* [Rockfall Detection on Moon](https://www.kaggle.com/datasets/yash92328/rockfall-detection-on-moon) from Kaggle.

## Dataset Structure




## 🛠 Installation

### Requirements
- Python                    3.10.9 
- ultralytics               8.1.20
- pillow                    9.4.0   
- opencv-python-headless    4.9.0.80   
- streamlit                 1.28.0    
- matplotlib                3.7.0    
     
## Packages
- libgl1 

## 👁Object Detection Model
- best.pt  : Trained Model File


# 🖥 Deployment
- Install the dependencies locally.

- To deploy this project:

```bash
  streamlit run app.py
```

- It will launch the webapp
- Select the image. You can get more images from the Dataset.
- It detects rockfall by drawing bounding boxes.

## 🧠 Hyperparameters

| Hyperparameters             | Values                                                              |
| ----------------- | ------------------------------------------------------------------ |
| Epoch  | 80  |
| imgsz | 640|



## 📷 Screenshot
![Finaloutput](https://github.com/ShrirangKanade/Obstacle_Detection_on_Lunar_Surface_using_U-Net/assets/110344056/8c183d67-d35c-4d69-bdff-c174b43073d4)


## 😇 Feedback

If you have any feedback, please reach out to us at coder.shrirang.kanade@gmail.com
