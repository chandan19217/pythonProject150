# -*- coding: utf-8 -*-
"""human_or_horse_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zTI5Ete5C1QdVvMx5IAquUoXgZhHVf5a

# Project: Horse or Human Classification using CNN
We have data for training:

500 horse images
527 human(male & female) images

For validation:

122 horse images
123 human(male & female) images

## Problem Statement:

Classifie given image is horse or human(male/female)

### Solution:

To solve this problem we are going to use Deep Learning Algorithm that is CNN (Convolutional Neural Network)

## Dara Scource

Raw Data Scource: https://www.kaggle.com/sanikamal/horses-or-humans-dataset

## Load Libraries
"""

import matplotlib.pyplot as plt

import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
##
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2

keras.__version__

"""## Load Data"""

train_data_path = "/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/train"
validation_data_path = "/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/validation"

"""# Data Preprocessing"""

training_datagen = ImageDataGenerator(rescale=1. / 255,
                                      rotation_range=40,
                                      width_shift_range=0.2,
                                      height_shift_range=0.2,
                                      shear_range=0.2,
                                      zoom_range=0.2,
                                      horizontal_flip=True,
                                      fill_mode='nearest')

training_data = training_datagen.flow_from_directory(train_data_path,
                                                     target_size=(150, 150),
                                                     batch_size=32,
                                                     class_mode='binary')

training_data.class_indices

valid_datagen = ImageDataGenerator(rescale=1. / 255)

valid_data = valid_datagen.flow_from_directory(validation_data_path,
                                               target_size=(150, 150),
                                               batch_size=32,
                                               class_mode='binary')


def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()


images = [training_data[0][0][0] for i in range(5)]
plotImages(images)

"""#Building cnn model"""

# Building cnn model
cnn_model = keras.models.Sequential([
    keras.layers.Conv2D(filters=32, kernel_size=7, input_shape=[150, 150, 3], kernel_regularizer=l2(l=0.01)),
    BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Conv2D(filters=64, kernel_size=5),
    BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Conv2D(filters=128, kernel_size=3),
    BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Conv2D(filters=256, kernel_size=3),
    BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Flatten(),  # neural network beulding
    keras.layers.Dense(units=128, activation='relu'),  # input layers
    BatchNormalization(),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(units=256, activation='relu'),
    BatchNormalization(),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(units=2, activation='softmax')  # output layer
])

# compile cnn model
cnn_model.compile(optimizer=Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model_path = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/horse_or_human_predictor.h5'
checkpoint = ModelCheckpoint(model_path, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

# train cnn model
history = cnn_model.fit(training_data,
                        epochs=100,
                        verbose=1,
                        validation_data=valid_data,
                        callbacks=callbacks_list)

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()# -*- coding: utf-8 -*-
"""human_or_horse_prediction.ipynb
 
Automatically generated by Colaboratory.
 
Original file is located at
    https://colab.research.google.com/drive/1zTI5Ete5C1QdVvMx5IAquUoXgZhHVf5a
 
# Project: Horse or Human Classification using CNN
We have data for training:
 
500 horse images
527 human(male & female) images
 
For validation:
 
122 horse images
123 human(male & female) images
 
## Problem Statement:
 
Classifie given image is horse or human(male/female)
 
### Solution:
 
To solve this problem we are going to use Deep Learning Algorithm that is CNN (Convolutional Neural Network)
 
## Dara Scource
 
Raw Data Scource: https://www.kaggle.com/sanikamal/horses-or-humans-dataset
 
## Load Libraries
"""

import matplotlib.pyplot as plt

import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
##
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2

keras.__version__

"""## Load Data"""

train_data_path = "/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/train"
validation_data_path = "/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/validation"

"""# Data Preprocessing"""

training_datagen = ImageDataGenerator(rescale=1./255,
                                      rotation_range=40,
                                      width_shift_range=0.2,
                                      height_shift_range=0.2,
                                      shear_range=0.2,
                                      zoom_range=0.2,
                                      horizontal_flip=True,
                                      fill_mode='nearest')

training_data =  training_datagen.flow_from_directory(train_data_path,
                                      target_size=(150, 150),
                                      batch_size=32,
                                      class_mode='binary')

training_data.class_indices

valid_datagen = ImageDataGenerator(rescale=1./255)

valid_data =  valid_datagen.flow_from_directory(validation_data_path,
                                      target_size=(150, 150),
                                      batch_size=32,
                                      class_mode='binary')

def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
    plt.tight_layout()
    plt.show()

images = [training_data[0][0][0] for i in range(5)]
plotImages(images)

"""#Building cnn model"""

#Building cnn model
cnn_model = keras.models.Sequential([
                                    keras.layers.Conv2D(filters=32, kernel_size=7, input_shape=[150, 150, 3],kernel_regularizer=l2(l=0.01)),
                                    BatchNormalization(),
                                    keras.layers.MaxPooling2D(pool_size=(2,2)),

                                    keras.layers.Conv2D(filters=64, kernel_size=5),
                                    BatchNormalization(),
                                    keras.layers.MaxPooling2D(pool_size=(2,2)),

                                    keras.layers.Conv2D(filters=128, kernel_size=3),
                                    BatchNormalization(),
                                    keras.layers.MaxPooling2D(pool_size=(2,2)),

                                    keras.layers.Conv2D(filters=256, kernel_size=3),
                                    BatchNormalization(),
                                    keras.layers.MaxPooling2D(pool_size=(2,2)),

                                    keras.layers.Flatten(), # neural network beulding
                                    keras.layers.Dense(units=128, activation='relu'), # input layers
                                    BatchNormalization(),
                                    keras.layers.Dropout(0.5),
                                    keras.layers.Dense(units=256, activation='relu'),
                                    BatchNormalization(),
                                    keras.layers.Dropout(0.5),
                                    keras.layers.Dense(units=2, activation='softmax') # output layer
])

# compile cnn model
cnn_model.compile(optimizer = Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model_path = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/horse_or_human_predictor.h5'
checkpoint = ModelCheckpoint(model_path, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

# train cnn model
history = cnn_model.fit(training_data,
                          epochs=100,
                          verbose=1,
                          validation_data= valid_data,
                          callbacks=callbacks_list)

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
"""
# Predict Horse or Human

Here we are loading train CNN model to predict Given input (image) is Horse of Human

# Import Libraries
"""

# Load Liraries
import numpy as np

import keras
from keras.preprocessing.image import ImageDataGenerator

"""# Import Model"""

model_path1 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/horse_human_cnn_model_new.h5'  # new model.ipynb
model_path2 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/horse_human_cnn_model_v2.h5'  # v2 solve overfitting Horse_or_human Classification using CNN.ipynb
model_path3 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/horse_human_cnn_model_v2_1.h5'  # v2 solve overfitting Horse_or_human Classification using CNN.ipynb

model1 = keras.models.load_model(model_path1)
model2 = keras.models.load_model(model_path2)
model3 = keras.models.load_model(model_path3)

"""#Preprocessing"""

# horse image path
h1 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/horse_test/horse1-204.png'
h2 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/horse_test/horse2-069.png'
h3 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/horse_test/horse3-070.png'
h4 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/horse_test/horse4-439.png'
h5 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/horse_test/horse5-203.png'
h6 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/horse_test/horse6-161.png'
h7 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/validation/horses/horse2-224.png'
h8 = "/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/validation/horses/horse5-123.png"

# human image path
hu1 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/human_test/valhuman01-09.png'
hu2 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/human_test/valhuman02-18.png'
hu3 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/human_test/valhuman03-23.png'
hu4 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/human_test/valhuman04-24.png'
hu5 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/test_data/human_test/valhuman05-19.png'
hu6 = '/content/drive/My Drive/My ML Project /DL Project/CNN/horse-or-human/dataset/validation/humans/valhuman01-13.png'

import numpy as np
from keras.preprocessing import image


def pred_human_horse(model, horse_or_human):
    test_image = image.load_img(horse_or_human, target_size=(150, 150))
    test_image = image.img_to_array(test_image) / 255
    test_image = np.expand_dims(test_image, axis=0)

    result = model.predict(test_image).round(3)

    pred = np.argmax(result)
    print(result, "--->>>", pred)

    if pred == 0:
        print('Predicted>>> Horse')
    else:
        print('Predicted>>> Human')


"""## Predict Output"""

for horse_or_human in [h1, h2, h3, h4, h5, h6, h7, h8, hu1, hu2, hu3, hu4, hu5, hu6]:
    pred_human_horse(model1, horse_or_human)

for horse_or_human in [h1, h2, h3, h4, h5, h6, h7, h8, hu1, hu2, hu3, hu4, hu5, hu6]:
    pred_human_horse(model2, horse_or_human)

for horse_or_human in [h1, h2, h3, h4, h5, h6, h7, h8, hu1, hu2, hu3, hu4, hu5, hu6]:
    pred_human_horse(model3, horse_or_human)