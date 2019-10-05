# Classification of the comments concerning a movie

import os

# Load the dataset
path = "/Users/morgane/Desktop/DL/aclImdb/"

train_pos = []
train_neg = []
test_pos = []
test_neg = []
comment = ''

for elt in os.listdir(path + "train/pos"):
    file = open(path + "train/pos/" + elt,'r')
    comment = file.read()
    file.close()
    train_pos.append(comment)

for elt2 in os.listdir(path + "train/neg"):
    file = open(path + "train/neg/" + elt2,'r')
    comment = file.read()
    file.close()
    train_neg.append(comment)

for elt3 in os.listdir(str((path + "‎test/pos").encode('ascii','ignore'))[1:].replace("'","")):
    file = open(str((path + "‎test/pos/" + elt3).encode('ascii','ignore'))[1:].replace("'",""),'r')
    comment = file.read()
    file.close()
    test_pos.append(comment)

for elt4 in os.listdir(str((path + "test/neg").encode('ascii','ignore'))[1:].replace("'","")):
    file = open(str((path + "test/neg/" + elt4).encode('ascii','ignore'))[1:].replace("'",""),'r')
    comment = file.read()
    file.close()
    test_neg.append(comment)

# encode('ascii','ignore') -> pour supprimer \u200e
# [1:] car b est ajouté lors de la précédente commande à la str
# replace("'","") car des ' sont ajoutés lors des précédentes commandes
#print(train_neg[50])