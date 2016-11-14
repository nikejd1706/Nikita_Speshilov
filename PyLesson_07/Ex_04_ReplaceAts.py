sentence = input("Please enter a sentence: ")

top = 0;

def replace():
    global top, sentence
    while top < sentence.count("a") > 0:
        sentence = sentence[0: sentence.index("a")] +"@"+ sentence[sentence.index("a")+1 : len(sentence)]

replace()
print("A's replaced with @'s is",sentence)
    
