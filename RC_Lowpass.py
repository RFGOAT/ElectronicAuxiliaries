#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:26:01 2017

@author: achim
"""
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import _RC_Calc_Class as rc
                
Heading = ['R[Ohm]','C[nF]','Cutoff fc[Hz]']

print('           _______                      \n' \
      '  Input____       __________Output      \n' \
      '           _______      |               \n' \
      '              R         |               \n' \
      '                     ___|___            \n' \
      '                     _______ C          \n' \
      '                        |               \n' \
      '                        |               \n' \
      '                       GND              \n' )

def RC_Calc():
    
    #Input
    eR           = int(input("Define the Resistors e-Series|Default e=24: ") or 24)
    eC           = int(input("Define the Capacitors e-Series|Default e=12: ") or 12)
    fc           = float(input("Cutoff Frequency fc [kHz]: ")) * 1000  #kilohertz input
    fc_tolerance = float(input("Cutoff Frequency Tolerance [Hz]|Default 100Hz: ") or 100)

    if (np.size( np.where(rc.RC_Calc.eValid == eR) ) > 0 and np.size( np.where(rc.RC_Calc.eValid == eC) ) > 0 ):
              
        #Calc factors and eSeries
        eSeriesR = rc.RC_Calc.Calc_ESeries(eR)
        eSeriesC = rc.RC_Calc.Calc_ESeries(eC)
        factorsR = rc.RC_Calc.Factors('R')
        factorsC = rc.RC_Calc.Factors('C')                    
         
        #create empty array              
        fcArr = np.empty((0,3), float)
    
        for f in range(0, factorsR.shape[0]):
            for r in range(0, eR):
                for c in range(0, eC):
                    
                    Res = factorsR[f,0]*eSeriesR[r]
                    Cap = factorsC[f,1]*eSeriesC[c]
                    fc_calc = 1/(2*np.pi * Res * Cap)
                    
                    if fc_calc < fc+fc_tolerance and fc_calc > fc-fc_tolerance:
                        
                        pairs = [factorsR[f,0]*eSeriesR[r], 1000000 * factorsC[f,1]*eSeriesC[c],fc_calc] #R   C[nF] , fc
                        pairs = np.round(pairs,3)
                        fcArr = np.append(fcArr, [pairs], axis=0)
                        
                        # plot frequency response                                        
                        sys = signal.lti(1,[2*np.pi*Res*Cap,1])
                        w, mag, phase = signal.bode(sys)
                        plt.semilogx(w, mag)
                        plt.axvline(fc_calc)       
                     
        #Printing
        np.set_printoptions(precision=5, suppress=True, threshold = np.nan)
        print('\n****OUTPUT***')
    
        if np.size(fcArr) > 0:
            print('Number of Combinations: ', fcArr.shape[0])
            print('\n')
            print(Heading)
            print('\n')
            print(fcArr)
            print('\n')
            
            plt.ylabel('Magnitude [dB]')
            plt.xlabel('Frequency [Hz]')
            plt.grid()
            plt.show()
        else:
            print('No combinations found, try a higher e-series, Increase tolerance!')
    
    else:
        print('\n\n***Series E6,E12,E24,E48,E96,E192 allowed only***\n\n')

while True:
    RC_Calc()

#RC_Calc()