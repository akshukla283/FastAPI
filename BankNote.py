# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:59:13 2020

@author: akshu
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float