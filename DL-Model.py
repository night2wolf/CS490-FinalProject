from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers import GaussianNoise
from keras.layers import GaussianDropout
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K

class DLModel:
  @staticmethod
  def BuildModel(Learning_Rate, Classes,Pic_Height,Pic_Width):
    pic_shape = (Pic_Height,Pic_Width)
    model = Sequential()
    # Input Layer
    model.add(Dense(512,activation='relu',inputshape=pic_shape))
    # First Hidden Layer
    model.add(Dense(512,activation='sigmoid'))
    #Second Hidden Layer convolution layer with Gaussian Noise
    model.add(Conv2D(32,(3,3),padding='same',activation='relu'))
    model.add(Activation('relu'))
    model.add(GaussianNoise(0.1))
    # Third hidden layer, convolution layer with dropout
    model.add(Conv2D(64,(3,3),padding='same',activation='relu'))
    model.add(Dropout(0.2))
    #Ouput Layer
    model.add(Dense(Classes,activation='softmax'))
    return model