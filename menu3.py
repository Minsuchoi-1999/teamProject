#!/usr/bin/python

def menu3():
    num_list1 = list(map(int, input("input the 1st list : ").split()));
    num_list2 = list(map(int, input("input the 2nd list : ").split()));

    print("union : ",list(set(num_list1) | set(num_list2)));
    print("intersection : ", list(set(num_list1) & set(num_list2)));

if __name__=="__main__" :
    menu3();
