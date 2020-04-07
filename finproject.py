import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

Datadir = "C:/Users/shubh/Downloads/Shubh_mypy_proj/CS5590/ICP/venv/deep_learning_project/PetImages"

categories = ["Dog", "Cat"]

training_data = []

img_size = 50


def create_training_data():
    for category in categories:
        path = os.path.join(Datadir, category)  # path to the categories
        class_num = categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()
print(len(training_data))
random.shuffle(training_data)

X = []
Y = []

for features, label in training_data:
    X.append(features)
    Y.append(label)

# Below reshaping is giving some error but required
# X = np.array(X).reshape(-1, img_size, img_size, 1)
# Y = np.array(Y).reshape(-1, img_size, img_size, 1)


# Below part I have not used
# pickle_out = open("X.pickle", "wb")
# pickle.dump(X, pickle_out)
# pickle_out.close()
#
#
# pickle_out = open("Y.pickle", "wb")
# pickle.dump(Y, pickle_out)
# pickle_out.close()
#
#
# pickle_in = open("X.pickle", "rb")
# X = pickle.load(pickle_in)
