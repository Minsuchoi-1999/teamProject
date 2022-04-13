#!/usr/bin/python

def function(name, num):
    fp = open(name, "r")
    lines = fp.readlines()
    for line in lines:
        word = line.split();
        print(word)
    fp.close


if __name__ == '__main__':
    function("word_freq.txt",10)
