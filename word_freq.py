#!/usr/bin/python

def function(name, num):
    words = []
    D = {}
    fp = open(name, "r")
    lines = fp.readlines()
    
    for line in lines:
        line = line.replace('.',' ').replace(',', ' ').replace('!', ' ').replace("'",' ').replace('-',' ')
        word = line.split()
        words.extend(word)

    set(words)

    for word in words:
        D[word] =0
        for line in lines:
            D[word] += line.count(word)
        
    Dlist = D.items()
    for d in Dlist:
        print(d)
    fp.close


if __name__ == '__main__':
    function("word_freq.txt",10)
