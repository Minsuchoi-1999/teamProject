#!/usr/bin/python

def fibo():
	n=int(input("fibonacci number: "))
	a,b=0,1

	for i in range(n):
		print(a, end = ' ')
		if i == n-1:
			print("\nF",n,"=", a)
		a,b=b,a+b 
if __name__=="__main__":
	print()
