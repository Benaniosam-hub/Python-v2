sentence = "Ai is powerful and smart"
sentence = sentence.lower()
words = set(sentence)
words.discard(" ")
for word in words:
    print(word,"-",sentence.count(word))