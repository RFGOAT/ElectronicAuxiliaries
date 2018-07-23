# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 07:20:42 2017

@author: U2683327
"""

import numpy as np

class RC_Calc ():
    
    eValid = np.array([3,6,12,24,48,96,192])
    
    def Calc_ESeries (e):
        
        #Resistor/Capacitor values
        k = np.arange(0,e)
        
        if e > 24:
            decimals =2
        else:
            decimals=1
            
        eSeries =np.round(10**(k/e),decimals)
        
        #Rundungsregeln exceptions
        if e == 3:
            eSeries[2] = 4.7
        if e == 6:
            eSeries[3] = 3.3
            eSeries[4] = 4.7
        if e == 12:
            eSeries[5] = 2.7
            eSeries[6] = 3.3
            eSeries[7] = 3.9
            eSeries[8] = 4.7
            eSeries[11] = 8.2
        if e == 24:
            eSeries[10] = 2.7
            eSeries[11] = 3.0
            eSeries[12] = 3.3
            eSeries[13] = 3.6
            eSeries[14] = 3.9
            eSeries[15] = 4.3
            eSeries[16] = 4.7
            eSeries[22] = 8.2
        if e == 192:
            eSeries[185] = 9.2
                   
        return eSeries
           
                        
    
    def Factors (R_or_C):
        
        if R_or_C == 'R':
            
            factors = np.array(
              [[1,1],       [1,10],      [1,100],      [1,1000],      [1,10000],      [1,100000],
               [10,1],      [10,10],     [10,100],     [10,1000],     [10,10000],     [10,100000],
               [100,1],     [100,10],    [100,100],    [100,1000],    [100,10000],    [100,100000],   
               [1000,1],    [1000,10],   [1000,100],   [1000,1000],   [1000,10000],   [1000,100000],
               [10000,1],   [10000,10],  [10000,100],  [10000,1000],  [10000,10000],  [10000,100000],
               [100000,1],  [100000,10], [100000,100], [100000,1000], [100000,10000], [100000,100000],
              ]
              )
            return factors
        if R_or_C == 'C':
            
            factors = np.array(
              [[10**-11,10**-11],  [10**-11,10**-10],[10**-11,10**-9],[10**-11,10**-8],[10**-11,10**-7],[10**-11,10**-6],
               [10**-10,10**-11],  [10**-10,10**-10],[10**-10,10**-9],[10**-10,10**-8],[10**-10,10**-7],[10**-10,10**-6],
               [10**-9,10**-11],   [10**-9,10**-10], [10**-9,10**-9], [10**-9,10**-8], [10**-9,10**-7], [10**-9,10**-6],   
               [10**-8,10**-11],   [10**-8,10**-10], [10**-8,10**-9], [10**-8,10**-8], [10**-8,10**-7], [10**-8,10**-6],
               [10**-7,10**-11],   [10**-7,10**-10], [10**-7,10**-9], [10**-7,10**-8], [10**-7,10**-7], [10**-7,10**-6],
               [10**-6,10**-11],   [10**-6,10**-10], [10**-6,10**-9], [10**-6,10**-8], [10**-6,10**-7], [10**-6,10**-6],
              ]
              )
            return factors
        else:
            print('No allowed character')
            
            
            
            
            
            