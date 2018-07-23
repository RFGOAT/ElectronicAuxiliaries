# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:51:43 2017

@author: U2683327
"""
import numpy as np
import _RC_Calc_Class as rc

Heading = ['R1[Ohm]','R2[Ohm]', 'Rp[Ohm]']

print('Calculates R1 & R2 for given R_parallel')

def CalcParRes () :
    
    #Inputs
    print('\n****INPUT****')
    e               = int(input("Define the Resistors e-series|Default e=24: ") or 24)
    R_ges           = float(input("Parallel Resistance [Ohm]: "))
    R_par_tolerance = float(input("Tolerance [Ohm]|Default=1: ") or 1)
    
    if (np.size( np.where(rc.RC_Calc.eValid == e) ) > 0):
        
        #Calc factors and eSeries
        eSeries = rc.RC_Calc.Calc_ESeries(e)
        factors = rc.RC_Calc.Factors('R')
                    
        #create empty array
        R_parArr = np.empty((0,3), float)
        
        #Calculation
        for f in range(0, factors.shape[0]):
            for r1 in range(0, e):
                for r2 in range(0, e):
                    
                    Res1 = factors[f,0]*eSeries[r1]
                    Res2 = factors[f,1]*eSeries[r2]
                    R_par = (Res1*Res2) / (Res1+Res2)
                    
                    #sort out the good Values
                    if R_par < R_ges+R_par_tolerance and R_par > R_ges-R_par_tolerance :
                        
                        pairs = [Res1, Res2, R_par]
                        pairs = np.round(pairs,3)
                        R_parArr = np.append(R_parArr, [pairs], axis=0)
          
        #Printing   
        np.set_printoptions(precision=3, suppress=True, threshold=np.nan)
        print('\n****OUTPUT*** \n')
                  
        if np.size(R_parArr) == 0:
            print('Increase tolerance!')
        else:
            print(Heading)
            print('\n')
            print(R_parArr)
        
    else:
        print('\n\n***Series E6,E12,E24,E48,E96,E192 allowed only***\n\n')

                
while True:
    CalcParRes()
#CalcParRes()