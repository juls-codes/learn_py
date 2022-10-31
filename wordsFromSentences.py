#Date created: October 27, 2022
#Program for displaying unique words

sentenceList = []
sentence = input("Enter a sentence: ")
while sentence != ("!!!"):
    sentenceList.append(sentence)
    sentence = input("Enter a sentence. Submit '!!!' to end sentence entry: ")

wordList = []
for sentence in sentenceList:
    wordList.extend(sentence.split())

wordUnique = []
for word in wordList:
    word = word.upper()
    word = word.replace(".","")
    word = word.replace(",","")
    if word not in wordUnique:
        wordUnique.append(word)

for word in wordUnique:
    print(word)
