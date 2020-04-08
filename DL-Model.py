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
  def BuildModel(Learning_Rate, Classes):
    model = Sequential()
    

    return model