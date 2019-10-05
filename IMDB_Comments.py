# Classification of the reviews concerning a movie

import os
from keras.models import Sequential
from keras.layers import Dense

# Load the dataset
path = "/Users/morgane/Desktop/DL/test reduit/"

# Fonction pour supprimer la ponctuation
def delPonct(texte):
    texte.replace(",","").replace("!","").replace(".","").replace("?","").replace(";","").replace('"','').replace("(","").replace(")","").replace('/','').replace('>','').replace('<','')
    return(texte)

# Fonction qui cree un dictionnaire de mots avec leur frequence, ordonné par ordre croissant d'apparition du mot
def frqWords(listWords):
    v = 0
    i1 = 0
    d = dict()
    i2 = 1
    while i1<len(listWords):
        while i2<len(listWords):
            if listWords[i1] == listWords[i2]:
                v = v+1
                del listWords[i2]
                i2 = i2 - 1
            i2 = i2 + 1
        if v != 0:
            d[listWords[i1]] = v
            v = 0
        del(listWords[i1])
        i2 = 1
        #print(len(d))
    sorted(d.items(), key=lambda t: t[1])
    return d

def removeUselessWords(words):
    uselessWords = ['this', 'the', 'a', 'for', 'of', 'i', 'he', 'she', 'they', 'movie', 'in', 'on', 'or', 'with', 'when', 'that', 'is', 'was', 'were', 'an', 'who', 'will', 'be', 'as', 'it', 'from', 'some', "it's", 'about', 'his', 'her', 'has', 'we', 'have', 'while', 'its', 'so', 'them', "there's"]
    i = 0
    while i < len(words):
        if words[i] in uselessWords:
            del(words[i])
            i = i-1
        i = i+1


train_pos = ""
train_neg = ""
test_pos = ""
test_neg = ""
comment = ''


# # # # TRAIN # # # #

for elt in os.listdir(path + "train/pos"):
    file = open(path + "train/pos/" + elt,'r')
    comment = file.read()
    train_pos = train_pos + comment
    file.close()

delPonct(train_pos)
words = train_pos.lower().split()
removeUselessWords(words)

Xtrain = frqWords(words)
print(Xtrain)


for elt2 in os.listdir(path + "train/neg"):
    file = open(path + "train/neg/" + elt2,'r')
    comment = file.read()
    train_neg = train_neg + comment
    file.close()

delPonct(train_neg)
words = train_neg.lower().split()
removeUselessWords(words)

Ytrain = frqWords(words) # negative train
print(Ytrain)

# On prend le meme nb de mots pour chaque liste
if len(Xtrain)<=len(Ytrain):
    L = len(Xtrain)
    del(Ytrain[len(Xtrain):])
else:
    L = len(Ytrain)
    del(Xtrain[len(Ytrain):])



# # # # TEST # # # #

for elt in os.listdir(path + "test/pos"):
    file = open(path + "test/pos/" + elt,'r')
    comment = file.read()
    test_pos = test_pos + comment
    file.close()

delPonct(test_pos)
words = test_pos.lower().split()
removeUselessWords(words)

Xtest = frqWords(words)
print(Xtest)


for elt2 in os.listdir(path + "test/neg"):
    file = open(path + "test/neg/" + elt2,'r')
    comment = file.read()
    test_neg = test_neg + comment
    file.close()

delPonct(test_neg)
words = test_neg.lower().split()
removeUselessWords(words)

Ytest = frqWords(words) # negative train
print(Ytest)

# On prend le meme nb de mots pour chaque liste
if len(Xtest)<=len(Ytest):
    L = len(Xtest)
    del(Ytrain[len(Xtest):])
else:
    L = len(Ytest)
    del(Xtrain[len(Ytest):])



# # # # MODEL COMPILATION # # # #

model = Sequential()
model.add(Dense(12, input_dim=L, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(Xtrain, Ytrain, validation_data=(Xtest,Ytest), epochs=2, batch_size=50)
scores = model.evaluate(Xtest, Ytest)

print("Accuracy: %.2f%%" % (scores[1]*100))



# for elt2 in os.listdir(path + "train/neg"):
#     file = open(path + "train/neg/" + elt2,'r')
#     comment = file.read()
#     file.close()
#     train_neg.append(comment)
#
# for elt3 in os.listdir(str((path + "‎test/pos").encode('ascii','ignore'))[1:].replace("'","")):
#     file = open(str((path + "‎test/pos/" + elt3).encode('ascii','ignore'))[1:].replace("'",""),'r')
#     comment = file.read()
#     file.close()
#     test_pos.append(comment)
#
# for elt4 in os.listdir(str((path + "test/neg").encode('ascii','ignore'))[1:].replace("'","")):
#     file = open(str((path + "test/neg/" + elt4).encode('ascii','ignore'))[1:].replace("'",""),'r')
#     comment = file.read()
#     file.close()
#     test_neg.append(comment)
#
# # encode('ascii','ignore') -> pour supprimer \u200e
# # [1:] car b est ajouté lors de la précédente commande à la str
# # replace("'","") car des ' sont ajoutés lors des précédentes commandes
# #print(train_neg[50])
#
# model = Sequential()
#
# result = dict()
