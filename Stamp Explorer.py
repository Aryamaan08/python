# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:25:59 2018

@author: Admin
"""
print("Welcome to Stamp Explorer! \n")
c = 0 #counter
countries = []
while c < 1: #Is the number of stamps a number?
    nos = input("How many stamps do you want to register: ") #nos is number of stamps
    try:
        int(nos) == (2, 1000)
        print("\n Moving on... \n")
        c = c + 1
    except ValueError:
        print("\n Please enter the number of stamps you want you enter!")
        c = 0
        nos = input("How many stamps do you want to register: ")
c = c + 1
nos = int(nos)
c = 0 #recycle #1
while c < nos: #Input: countries
    countries.append(input("Enter the country from where your stamp is from: "))
    c = c + 1
c = 0 #recycle #2
n = 0 #counter
while c < (nos - 1): #duplicate removal
    c = c + 1
    while (n < (nos - 1) and c < (nos - 1)):
        if countries[c] == countries[n]: 
            del(countries[n])
            nos = nos - 1
        else:
            n = n + 1
nos_str = str(nos)
print("You have stamps of " + nos_str + " unique countries.")
print("The countries are: ")
print(countries)