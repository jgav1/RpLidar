#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:48:09 2018

@author: Jorge Aragon
"""
# Para lectura de datos base en panda

import pandas as pd

file = 'Lidar 1.xlsx'
sheet= 'last_capture'
angle= 3
distance= 4

liA = pd.read_excel(file,sheet)
liD = pd.read_excel(file,sheet)
pd.concat([liA,liD])



