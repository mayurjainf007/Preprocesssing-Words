from nltk.corpus import wordnet
syns = wordnet.synsets("program")
##print(syns)
##print(syns[0])
##print(syns[0].lemmas())

#synset
print(syns[0].name())

#just the word
##print(syns[0].lemmas()[0].name())

#definition
##print(syns[0].definition())

#examples
##print(syns[0].examples())

##synonyms=[]
##ant=[]
##for syn in wordnet.synsets("good"):
##    for l in syn.lemmas():
####        print("l:",l)
##        synonyms.append(l.name())
##        if l.antonyms():
##           print(l.antonyms())
######            antonyms.append(l.antonyms()[0].name())
##print(set(synonyms))
##print(set(antonyms))


# similarity of two words 
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))
##
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))






            
