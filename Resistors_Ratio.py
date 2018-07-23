#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:26:01 2017

@author: achim
"""

import numpy as np
import _RC_Calc_Class as rc

Heading = ['R1[Ohm]','R2[Ohm]', 'R1+R2[Ohm]', 'Ratio']

print('Defines the ratio as:  Ratio = R1/R2')

               
def Res_from_Ratio():

    #Input
    print('\n****INPUT***\n')
    e         = int(input("Define the Resistors e-Series|Default e=24: ") or 24)
    ratio      = float(input("Define the Resistors Ratio [%]: ") ) / 100
    Ratio_tol  = float(input("Ratio Tolerance [%]|Default 0.5%: ") or 0.5)       
       
    if (np.size( np.where(rc.RC_Calc.eValid == e) ) > 0):
            
        #Calc factors and eSeries
        eSeries = rc.RC_Calc.Calc_ESeries(e)
        factors = rc.RC_Calc.Factors('R')
    
        #create empty array
        RatioArr = np.empty((0,4), float)
    
        #Calculations
        for f in range(0, factors.shape[0]):
            for r1 in range(0, e):
                for r2 in range(0, e):
                    
                    Res1 = factors[f,0]*eSeries[r1]
                    Res2 = factors[f,1]*eSeries[r2]
                    ratio_calc = Res1/Res2
                    
                    if ratio_calc < ratio+Ratio_tol/100*ratio and ratio_calc > ratio-Ratio_tol/100*ratio:
                            
                        pairs = [Res1, Res2, Res1+Res2, ratio_calc] #r1, r2, R1+r2, ratio
                        pairs = np.round(pairs,3)
                        RatioArr = np.append(RatioArr, [pairs], axis=0)
                        
        #Printing
        np.set_printoptions(precision=3, suppress=True, threshold = np.nan)
        print('\n****OUTPUT***')
    
        if np.size(RatioArr) > 0:
            print('Number of Combinations: ', RatioArr.shape[0] )
            print('\n')
            print(Heading)
            print('\n')
            print(RatioArr)
            print('\n')
        else:
            print('No combinations found, try a higher e-series, Increase tolerance!')
            
    else:
        print('\n\n***Series E6,E12,E24,E48,E96,E192 allowed only***\n\n')

while True:
    Res_from_Ratio()

#Res_from_Ratio()
