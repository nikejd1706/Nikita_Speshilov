sentence = input("Please enter a sentence: ")
def replace(sn):
    if (" " not in sn):
        return sn
    else:
        return sn[0:sn.index(" ")] + "_" + replace(sn[sn.index(" ")+1 : len(sn)])

print(replace(sentence))

        
