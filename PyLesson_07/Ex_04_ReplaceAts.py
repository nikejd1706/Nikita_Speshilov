sentence = input("Please enter a sentence: ")
top = 0;

def replace():
    global top, sentence
    while top < sentence.count("a") > 0:
        sentence = sentence[0: sentence.index("a")] + sentence[sentence.index("@")+1 : len(sentence)]

replace()
print(sentence)
    
