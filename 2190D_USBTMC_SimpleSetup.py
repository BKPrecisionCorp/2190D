# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:47:15 2016

@author: eamezquita
"""

import visa   #Imports visa, package that helps you control instrumentation
    
try:
    #Open Connection
    rm = visa.ResourceManager()  #Creating a resource manager object
    rm.list_resources() #listing all available resources (COM Ports, etc)
    
    Oscope = rm.open_resource("USB0::0xF4EC::0xEE3A::464F14110::INSTR")
    Oscope.timeout =  5000
    
    Oscope.write ("ASET") # automatically adjusts controls to produce a usable display of the input signal.
    
     
    Oscope.write("C1:CPL?")# Is is cuopled?
  
    
    #Oscope.write ("TRMD SINGLE;ARM;FRTR") #instrument makes one acquisition
    
    Oscope.write ("STOP") #  immediately stops the acquisition of a signal. If the trigger mode is AUTO or NORM.
       
    
    Oscope.close()#close port
        
finally:
    #perform clean up operations
    print ('complete')
