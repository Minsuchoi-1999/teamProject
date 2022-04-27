# HW06 Team Project main script

import menu3
import b2h
#import fibo

if __name__=="__main__" :
  menu = 0
  while True:
      menu = int(input("Select menu: 1)b2h 2)set 3)fibo 4)exit ? "))
      if menu == 1:
          b2h.b2h()
      if menu == 2:
          menu3.menu3()
      if menu == 3:
          #fibo.fibo()
          print("ex")
      if menu == 4:
          break
