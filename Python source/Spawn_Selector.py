import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, Rescaling
import numpy as np


data_dir = "result"

img_height = 480
img_width = 480
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names


AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

model = Sequential()
model.add(Rescaling(1./255, input_shape=(img_height, img_width, 3))),
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


hist = model.fit(train_ds, epochs=1, validation_data=val_ds,
                 steps_per_epoch=256)


def predict_data():
    img = tf.keras.utils.load_img(
        'test.jpg', target_size=(480, 480)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )


predict_data()
new_model = model.save('saved_models/last_model.keras')