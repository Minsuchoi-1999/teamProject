#!/usr/bin/python

print("input the 1st list:");
num_list1 = list(map(int, input().split()));
print("input the 2nd list:");
num_list2 = list(map(int, input().split()));

print("union : ",list(set(num_list1) | set(num_list2)));
print("intersection : ", list(set(num_list1) & set(num_list2)));
