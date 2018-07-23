#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:26:01 2017

@author: achim
"""

import numpy as np
import _RC_Calc_Class as rc
import matplotlib.pyplot as plt

Heading = ['R1[Ohm]','R2[Ohm]', 'Value']

print('Defines the ratio as:  Ratio = R1/R2')

               
def AnyCalc():

    #Input
    print('\n****INPUT***\n')
    e         = int(input("Define the Resistors e-Series|Default e=24: ") or 24)
    value      = float(input("Define value ") )
    tolerance  = float(input(" Tolerance [%]|Default 0.5%: ") or 0.5)       
       
    if (np.size( np.where(rc.RC_Calc.eValid == e) ) > 0):
            
        #Calc factors and eSeries
        eSeries = rc.RC_Calc.Calc_ESeries(e)
        factors = rc.RC_Calc.Factors('R')
    
        #create empty array
        ValueArr = np.empty((0,3), float)
    
        #Calculations
        for f in range(0, factors.shape[0]):
            for r1 in range(0, e):
                for r2 in range(0, e):
                    
                    Res1 = factors[f,0]*eSeries[r1]
                    Res2 = factors[f,1]*eSeries[r2]
                    
                    "DEFINE Formula HERE"#############################
                    value_calc = 1.25*(1+(Res2/Res1)) + (50*10**-6*Res2)
                    "DEFINE Formula HERE"#############################
                    
                    if value_calc < value+tolerance/100*value and value_calc > value-tolerance/100*value:
                            
                        pairs = [Res1, Res2, value_calc] #r1, r2, ratio
                        pairs = np.round(pairs,3)
                        ValueArr = np.append(ValueArr, [pairs], axis=0)
                        
        #Printing
        np.set_printoptions(precision=3, suppress=True, threshold = np.nan)
        print('\n****OUTPUT***')
    
        if np.size(ValueArr) > 0:
            print('Number of Combinations: ', ValueArr.shape[0] )
            print('\n')
            print(Heading)
            print('\n')
            print(ValueArr)
            print('\n')
            plt.plot(np.arange(len(ValueArr[:,2])),ValueArr[:,2])
            plt.plot(np.arange(len(ValueArr[:,2])),np.ones(len(ValueArr[:,2]))*value,'r')
            plt.grid()
            plt.show()
        else:
            print('No combinations found, try a higher e-series, Increase tolerance!')
            
    else:
        print('\n\n***Series E6,E12,E24,E48,E96,E192 allowed only***\n\n')

while True:
    AnyCalc()

#AnyCalc()
