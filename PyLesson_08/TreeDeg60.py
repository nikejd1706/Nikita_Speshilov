word = input("Please enter a word: ")
start = 0
stop = len(word)

def tree(word, start, stop):
    if start <= stop:
        print 
        start += 1
        tree(word, start, stop)

tree(word, start, stop)
    
