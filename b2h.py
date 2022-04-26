#!/usr/bin/python

print("input bin number: ", end ="")

binary_value = input()
decimal_value = int(binary_value, base = 2)
hex_value = hex(decimal_value)

print("hexa number:", hex_value)

