#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:34:58 2017

@author: achim
"""
import numpy as np
import _RC_Calc_Class as rc

Heading = ['ratio','R1[Ohm]', 'R2[Ohm]', 'Rges[Ohm]', 'Ibias(R2)[mA]', 'Uout[V]']

print('   VDD           \n' \
      '    |            \n' \
      ' R1| |           \n' \
      '   | |           \n' \
      '    |            \n' \
      '    |-----       \n' \
      '    |    |       \n' \
      ' R2| |  | |Rload \n' \
      '   | |  | |      \n' \
      '    |    |       \n' \
      '   GND  GND      \n')

def VoltageDiv():
    
    #Inputs
    print('\n****INPUT***')
    e       = int(input("Define the Resistors e-Series|Default e=24: ") or 24)
    U_in    = float(input("Input Voltage [V]: "))
    U_out   = float(input("Output Voltage [V]: "))
    R_load  = float(input("Load Resistance [Ohm]|Default: 1GOhm ") or 999999999)
    I_bias  = float(input("Bias current (R2) [mA]|Default: 2mA ") or 2)
    
    U_ratio_tolerance = float(input("Output Voltage Tolerance [%] | Default 1%: ") or 1)
    I_bias_tolerance = float(input("Bias Current Tolerance [%] | Default 50%: ") or 50)
    I_bias_tolerance = I_bias_tolerance/100 # calc ratio
    U_ratio_tolerance = U_ratio_tolerance/100 # calc ratio
    
    if (np.size( np.where(rc.RC_Calc.eValid == e) ) > 0):
        
        #Calc factors and eSeries
        eSeries = rc.RC_Calc.Calc_ESeries(e)
        factors = rc.RC_Calc.Factors('R')
        
        #Calc ratio
        Uratio = U_out/U_in    
        #create empty array
        RratioArr = np.empty((0,6), float)
            
        #Calculations
        for f in range(0, factors.shape[0]):
            for r1 in range(0, e):
                for r2 in range(0, e):
                    
                    Res1 = factors[f,0]*eSeries[r1]
                    Res2 = factors[f,1]*eSeries[r2]
                    R_par = Res2*R_load / (Res2+R_load)
                    Rratio = R_par/(Res1+R_par)
                    
                    #sort out the good ratio
                    if Rratio < Uratio+U_ratio_tolerance*Uratio and Rratio > Uratio-U_ratio_tolerance*Uratio : #Voltage
                        
                        U = Rratio*U_in
                        I = U/Res2*1000 # mA
                        
                        if I < I_bias+I_bias_tolerance*I_bias and I > I_bias-I_bias_tolerance*I_bias: #Ibias
                            
                            pairs = [Rratio, factors[f,0]*eSeries[r1], factors[f,1]*eSeries[r2],R_par+Res1, I, U] #ratio, r1, r2, Rges, I, U out
                            pairs = np.round(pairs,3)
                            RratioArr = np.append(RratioArr, [pairs], axis=0)
        
        #Printing
        np.set_printoptions(precision=3, suppress=True, threshold = None)
        print('\n****OUTPUT***')
        print('Voltage Ratio Uout/Uin: %2.2f'% Uratio)
        
        if np.size(RratioArr) > 0:
            print('Number of Combinations: ', RratioArr.shape[0] )
            print('\n')
            print(Heading)
            print('\n')
            print(RratioArr)
        else:
            print('No combinations found, try a higher e-series!')
    
    else:
        print('\n\n***Series E6,E12,E24,E48,E96,E192 allowed only***\n\n')
  
    
while True:
    VoltageDiv()
