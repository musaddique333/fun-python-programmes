#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:05:00 2022

@author: mohmmadmusaddique
"""
import os
import numpy as np
while 1:      
    print('\f')
    print('Guess The Number')
    number = np.random.randint(1,100)
    
    for i in range(0,8):
        
        print('your guess')
        print(8-i,'Guesses left!!\n\n')
        num=int(input(" "))
        
        if num > number:
            print('oops you entered larger number try again')
        elif num < number:
            print('oops you entered smaller number try again')
        elif num == number:
            print('\ncongratulations you guessed the correct number\n')
            print('\nyou used ',i+1,' guesses to win\n')
            break
        
        if i==7:
            print('GaMe OvEr !!')
            print('\n\n')
            break
    print('enter "yes" to play again anything else to exit the game')
    ans=input()
    if ans=='yes':
        continue
    else:
        print('\f')
        break
