# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 10:45:42 2017

@author: Felipe
"""

import matriz as mtz

A = mtz.matriz(mtz.digitar_matriz())
M, I = A.inv_gj()
print(I)
