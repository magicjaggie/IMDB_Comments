# Classification of the reviews concerning a movie

import os

# Fonction pour supprimer la ponctuation
def delPonct(texte):
    texte.replace(",","").replace("!","").replace(".","").replace("?","").replace(";","").replace('"','').replace("(","").replace(")","").replace('/','').replace('>','').replace('<','')
    return(texte)

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
    words = delPonct(comment).lower().split()
    train_pos.append(words)

for elt2 in os.listdir(path + "train/neg"):
    file = open(path + "train/neg/" + elt2,'r')
    comment = file.read()
    file.close()
    words = delPonct(comment).lower().split()
    train_neg.append(words)

for elt3 in os.listdir(str((path + "‎test/pos").encode('ascii','ignore'))[1:].replace("'","")):
    file = open(str((path + "‎test/pos/" + elt3).encode('ascii','ignore'))[1:].replace("'",""),'r')
    comment = file.read()
    file.close()
    words = delPonct(comment).lower().split()
    test_pos.append(words)

for elt4 in os.listdir(str((path + "test/neg").encode('ascii','ignore'))[1:].replace("'","")):
    file = open(str((path + "test/neg/" + elt4).encode('ascii','ignore'))[1:].replace("'",""),'r')
    comment = file.read()
    file.close()
    words = delPonct(comment).lower().split()
    test_neg.append(words)

# encode('ascii','ignore') -> pour supprimer \u200e
# [1:] car b est ajouté lors de la précédente commande à la str
# replace("'","") car des ' sont ajoutés lors des précédentes commandes
#print(train_neg[50])


# Model
model=Sequential()
model.add(Embedding(5000,32,input_lenght = 500)) # Less than 500 words for each review, consider 5000 words for the voc
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())


# Fit the model
model.fit(train_pos, train_neg, validation_data=(test_pos, test_neg), epochs=2, batch_size=128, verbose=2)
# Final evaluation of the model
scores = model.evaluate(test_pos, test_neg, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))