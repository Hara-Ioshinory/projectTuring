import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, Rescaling
import numpy as np

def create_a_Model():
    img_height = 480
    img_width = 480
    batch_size = 32

    model = Sequential()
    model.add(Rescaling(1. / 255, input_shape=(img_height, img_width, 3))),
    model.add(Conv2D(8, (3, 3), 1, activation='relu', padding='same', input_shape=(256, 256, 3)))
    model.add(MaxPooling2D())
    model.add(Conv2D(16, (3, 3), 1, activation='relu', padding='same'))
    model.add(MaxPooling2D())
    model.add(Conv2D(8, (3, 3), 1, activation='relu', padding='same'))
    model.add(MaxPooling2D())
    model.add(Dense(12, activation='relu'))
    model.add(Flatten())
    model.add(Dense(len(class_names)))
    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
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
