#!/usr/bin/python
# HW06 Team Project main script

import calcpkg.b2h
import calcpkg.menu3
import calcpkg.fibo

if __name__=="__main__" :
  menu = 0
  while True:
      menu = int(input("Select menu: 1)b2h 2)set 3)fibo 4)exit ? "))
      if menu == 1:
          calcpkg.b2h.b2h()
      if menu == 2:
          calcpkg.menu3.menu3()
      if menu == 3:
          calcpkg.fibo.fibo()
      if menu == 4:
          print("exit the program..")
          break
