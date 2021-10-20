#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:45:33 2021

@author: molierenguile-makao
"""

class Vectorp2d:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def proten(self):
        self.x = self.x**2
        self.y = self.x*self.y
        return self

    def repta(self):
        print("Cordonnée X : {}\n Cordonnée Y : {}".format(str(self.x),str(self.y)))
        
        