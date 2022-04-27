def fibo(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end = ' ')
        if i==n-1:
          print("\nF",n, "=",a)
        a, b = b, a+b
