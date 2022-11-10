# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:25:15 2022

@author: 62817
"""
print("Ordinal Number")

def ordinalnumber(n):
    n == number
    if n % 10 == 1:
        return n, "st"
    elif n % 10 == 2:
        return n, "nd"
    elif n % 10 == 3:
        return n, "rd"
    elif n % 10 in range(4, 21):
        return n, "th"
    elif n % 10 == 0:
        return n, "th"
    else:
        return ordinalnumber(n)

number = ""

while number != 0:
    number = int(input("Masukkan angka = "))
    print(ordinalnumber(number))
    