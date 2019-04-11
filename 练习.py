# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:27:45 2019

@author: dell
"""

class jifen:
    def __init__(self,f,n = 10**5):
        self.f = f
        self.n = n
    
    def __call__(self,w,x):
        result = 0
        for i in range(self.n):
            result += w(i)*self.f(x(i))
        return result

class middlepoint(jifen):
    def __call__(self,a,b):
        h = (b-a)/self.n
        def w(i):
            return (b-a)/self.n
        
        def x(i):
            return a + i*h +h/2
        return jifen.__call__(self,w,x)

class tixing(jifen):
    def __call__(self,a,b):
        h = (b-a)/self.n
        def w(i):
            if i == 0 or i == self.n - 1:
                return h
            else:
                return h/2
        def x(i):
            return a + i*h
        return jifen.__call__(self,w,x)
