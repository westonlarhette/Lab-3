#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:10:06 2024

@author: westonlarhette
"""

# Comp Lab 1200 2/5 Exercise 1
# Creating a vector via tuples
# =============================================================================
 import math
 x = float(input('Enter first vector component'));
 y = float(input('Enter second vector component'));
 vector = (x,y)
 magnitude = math.sqrt((vector[0])**2 + (vector[1])**2)
 print('The vectors magnitude is', magnitude)
# =============================================================================


# Create list of prime numbers and perform various operations on it
"""List of Prime Numbers"""
# =============================================================================
 list_prime = [1,2,3,5,7]
 list_prime.append(11)
 list_prime.append(13)
 
 new_list = list_prime[:3]
 print(list_prime[:3])
 
 list_new_prime = [17,19,23]
 list_prime.extend(list_new_prime)
 
 print(list_prime)
 
 print(list_prime[::-1])
 
 list_prime.reverse()
 
 print(list_prime)
# =============================================================================


# Create a dictionary using the 8 planets as keys and their 
# value for g as values
# Get the mass of the user in kg and their desired planet
# Use the planet the user enters to extract the value of
# its g from the dictionary and return the weight of the
# user on that planet

gs = {}
# g is in units m/s^2

gs["Mercury"] = 3.7
gs["Venus"] = 8.9
gs["Earth"] = 9.8
gs["Mars"] = 3.7
gs["Jupiter"] = 23.1
gs["Saturn"] = 9.0
gs["Uranus"] =8.7
gs["Neptune"] = 11

mass = input("Enter your mass in kg:")
mass = float(mass)
planet = input("Enter your chosen planet:")

weight = mass*gs[planet]

print("Weight on planet = ", weight,"N")








