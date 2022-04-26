#!/usr/bin/python

num_list1 = list(map(int, input().split()));

num_list2 = list(map(int, input().split()));

print("intersection : ");
print(set(num_list1) & set(num_list2));
print("\nunion : ");
print(set(num_list1) | set(num_list2));
