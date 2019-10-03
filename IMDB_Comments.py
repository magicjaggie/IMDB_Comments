# Classification of the comments concerning a movie

import os

# Load the dataset
path = "/Users/morgane/Desktop/DL/aclImdb/"

train_pos = ''
train_neg = ''
test_pos = ''
test_neg = ''
comment = ''

for elt in os.listdir(path + "train/pos"):
    file = open(elt,'r')
    comment = file.read()
    file.close()
    train_pos = train_pos + comment

for elt2 in os.listdir(path + "‎train/neg"):
    file2 = open(elt2,'r')
    comment2 = file2.read()
    file2.close()
    train_neg = train_neg + comment2

for elt3 in os.listdir(path + "‎test/pos"):
    file = open(elt3,'r')
    comment = file.read()
    file.close()
    test_pos = test_pos + comment

for elt4 in os.listdir(path + "test/neg"):
    file = open(elt4,'r')
    comment = file.read()
    file.close()
    test_neg = test_neg + comment

