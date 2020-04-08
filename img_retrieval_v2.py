import os
import cv2
import random

Datadir = "C:/Users/shubh/Desktop/tiny-imagenet-200/tiny-imagenet-200/train"

categories = os.listdir(Datadir)

training_data = []

limit = 1000  # can be customized depending on the size of data we want to use


def create_training_data():
    for category in categories:
        if len(training_data) < limit:
            path = os.path.join(Datadir + '/' + category + '/' + 'images')  # path to the categories
            class_num = category
            for img in os.listdir(path):
                try:
                    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)

                    training_data.append([img_array, class_num])
                except Exception as e:
                    pass
        random.shuffle(training_data)


create_training_data()
print(len(training_data))

X = []
Y = []

for features, label in training_data:
    X.append(features)
    Y.append(label)

print(training_data)
