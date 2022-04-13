#!/usr/bin/python

import operator
import sys

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
    for i in range(0,num):
        print('{:<10} {:>10}'.format(d1[i][0],d1[i][1]))
    fp.close
    


if __name__ == '__main__':
    address = sys.argv[1]
    number = int(sys.argv[2])

    function(address,number)
