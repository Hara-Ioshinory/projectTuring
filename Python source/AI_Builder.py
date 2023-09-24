import cv2
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

import numpy as np


def create_a_Model():
    model = Sequential()

    model = Sequential()
    model.add(Conv2D(8, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
    model.add(MaxPooling2D())
    model.add(Conv2D(16, (3, 3), 1, activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(8, (3, 3), 1, activation='relu'))
    model.add(MaxPooling2D())
    model.add(Flatten())
    model.add(Dense(2, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])
    model.summary()

def load_model(modelSRC):
    last_model = tf.keras.models.load_model(modelSRC)
    return last_model


cur_model = load_model('A:/saved_models/last_model.keras')
imgSRC = 'A:/result/Alarm_Peoples/123124.jpg'
img = cv2.imread(imgSRC)
h, w = (int(i) for i in img.shape[:2])
img_n =
print(cur_model.predict(img))
