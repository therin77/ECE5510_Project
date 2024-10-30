#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:28:44 2024

@author: kategothberg
"""

#ECE 5510 -  Computer Project
#Last Edit : 10/10/24
#Developed by Kate Gothberg

import numpy as np

class point():  
  
    def __init__(self, name, x, y, PEC):  
        self.name = name
        self.x = x  
        self.y = y  
        self.PEC = PEC
        
    def __str__(self):  
        return (f"{self.name}: "  
                f"x: {self.x}, "  
                f"y: {self.y} "  
                f"PEC: {self.PEC}"  
               )
        
        
points_list = [point( 0, -.015, 0, -1), point( 1, -.005, 0, -1), point( 2, .005, 0, -1), point( 3, .015, 0, -1),
               point( 4, -.015, .01, 0), point( 5, -.005, .01, -1), point( 6, .005, .01, -1), point( 7, .015, .01, 0),
               point( 8, -.015, .02, 0), point( 9, -.005, .02, 0), point( 10, .005, .02, 0), point( 11, .015, .02, 0)] 

print(points_list[4])

