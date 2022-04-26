# HW06 Team Project main script

menu = 0

while True:
    menu = int(input("Select menu: 1)b2h 2)set 3)fibo 4)exit ? "))
    
    if menu == 1:
        exec(open("b2h.py").read())
    if menu == 2:
        exec(open("menu3.py").read())
    if menu == 3:
        exec(open("fibo.py").read())
    if menu == 4:
        break
