#!/usr/bin/python

import operator

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
    d1 = sorted(Dlist, key=operator.itemgetter(1),reverse=True)
    print(d1)
    fp.close

    


if __name__ == '__main__':
    function("word_freq.txt",5)
