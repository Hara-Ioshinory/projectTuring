import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.metrics import Precision, Recall, BinaryAccuracy

import numpy as np
import cv2
from matplotlib import pyplot as plt

data_dir = "A:/result"
data = tf.keras.utils.image_dataset_from_directory(data_dir, labels='inferred')
class_names = data.class_names

data = data.map(lambda x, y: (x/255, y))
scaled_iterator = data.as_numpy_iterator()

train_size = int(len(data)*.7)
val_size = int(len(data)*.2)
test_size = int(len(data)*.1)

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)

model = Sequential()
model.add(Conv2D(16, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
model.add(MaxPooling2D())
model.add(Conv2D(16, (3, 3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(8, (3, 3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])
model.summary()

logdir = 'A:/logs'
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)
hist = model.fit(train, epochs=1, validation_data=val, callbacks=[tensorboard_callback])
#
#
# def predict_data():
#     img = tf.keras.utils.load_img(
#         'A:/result/Alarm_Peoples/123124.jpg', target_size=(480, 480)
#     )
#     img_array = tf.keras.utils.img_to_array(img)
#     img_array = tf.expand_dims(img_array, 0)  # Create a batch
#
#     predictions = model.predict(img_array)
#     score = tf.nn.softmax(predictions[0])
#
#     print(
#         "This image most likely belongs to {} with a {:.2f} percent confidence."
#         .format(class_names[np.argmax(score)], 100 * np.max(score))
#     )
#
#
# predict_data()
# new_model = model.save('A:/saved_models/last_model.keras')
