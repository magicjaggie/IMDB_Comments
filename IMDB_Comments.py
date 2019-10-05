# Classification of the reviews concerning a movie

import os
from keras.models import Sequential

# Load the dataset
path = "/Users/morgane/Desktop/DL/aclImdb/"

def delPonct(texte):
    texte.replace(",","").replace("!","").replace(".","").replace("?","").replace(";","").replace('"','').replace("(","").replace(")","")
    return(texte)

def frqWords(listWords):
    v = 0
    d = dict()
    for i1 in range(0,len(listWords)):
        for i2 in range(0,len(listWords)):
            if listWords[i1] == listWords[i2]:
                v = v+1
                if i1 != i2:
                    del listWords[i2]
                    i2 = i2-1
        if v != 0:
            d[listWords[i1]]=v
            del(listWords[i1])
            i1 = i1-1
            v = 0
    return(d)


train_pos = []
train_neg = []
test_pos = []
test_neg = []
comment = ''

for elt in os.listdir(path + "train/pos"):
    file = open(path + "train/pos/" + elt,'r')
    comment = file.read()
    delPonct(comment)
    words = comment.split()
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

model = Sequential()

result = dict()
