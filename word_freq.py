#!/usr/bin/python

def function(name, num):
    words = []
    fp = open(name, "r")
    lines = fp.readlines()
    for line in lines:
        line = line.replace('.',' ').replace(',', ' ').replace('!', ' ').replace('?',' ').replace('-',' ')
        word = line.split()
        words.extend(word)
    print(words)
    fp.close


if __name__ == '__main__':
    function("word_freq.txt",10)
