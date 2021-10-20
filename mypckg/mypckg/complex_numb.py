#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:59:16 2021

@author: molierenguile-makao
"""

class complexNbr:
    def __init__(self,a,b):
        self.Re=a
        self.Im=b
        
    def carre(self):
        self.Re=self.Re**2-self.Im**2
        self.Im=2*self.Im*self.Re
        return self 
    
    def rept(self):
        print({}+"+"+"i"+{}.format(str(self.Re),str(self.Im)))
        
        