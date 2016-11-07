sentence = input("Please enter a String: ")

top = 0
while top < sentence.count(" ") > 0:
    sentence = sentence[0: sentence.index]
    
