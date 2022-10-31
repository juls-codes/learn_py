#Date created: October 21, 2022
#Program for a word counter as a dictionary

#Loop for userInput while input is not empty. Put each userInput to list: SentenceList.
userInput=input("Type a sentence: ")
SentenceList = []

while userInput != (""):
    SentenceList.append(userInput)
    userInput=input("Type a sentence. To end sentence entry, submit a blank response: ")

# Extract each word from SentenceList. Put in new list: WordList
WordList = []

for sentence in SentenceList:
    WordList.extend(sentence.split())
    
#Count how many times each word occurs in WordList.
#Create dictionary with each word as key and count as value
WordDictionary = {}

for word in WordList:
    word = word.lower() #make case-insensitive
    word = word.replace(".","") #ignore punctuation -> replace . to empty
    if word in WordDictionary:
        WordDictionary[word] = WordDictionary[word] + 1
    else:
        WordDictionary[word] = 1

#Iterate through WordDictionary to display readable results
for word in WordDictionary.keys():
    print(word, ":", WordDictionary[word])
