# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:44:55 2019

@author: romain.biassin
"""

import matplotlib.pyplot as plt
import numpy as np



def insertion(T, Tft, alpha):
   dep = 50;
   #w = im.size;
   #h= im.size;
   w=256;
   h=256;
   alpha = 99999999999999999999999999
   print w;

   for i in range(0,32):
       for k in range(0,32): 
          # Tft[i+dep][k+dep] += 99999999999999999999999999999999999999* alpha*T[i/2]
           #Tft[i+168][k+18] += 99999999999999999999999999999999999999* alpha*T[i/2] #prendre l'image/2
          #Tft[i+w/2][k+h/2] += 99999999999999999999999999999999999999* alpha*T[i/2]
          #Tft[i-w/2][k-h/2] += 99999999999999999999999999999999999999* alpha*T[i][k]
          #Tft[i+w/2-32][k+h/2-32] += 99999999999999999999999999999999999999* alpha*T[i][k]
          Tft[i][k]+=(1-alpha*T[k])
          k=k+1
          #Tft[i-w/2-32][k-h/2-32] += 99999999999999999999999999999999999999* alpha*T[i/2]
          
           
   return Tft




im = plt.imread("cameraman.tif")
im= np.array(im)

#plt.figure()
#plt.imshow(im, "gray") #colormap binary
#plt.title("My title")

i2 = np.fft.fft2(im)
i2 = np.fft.fftshift(i2)


plt.figure()
mod = np.log10(abs(i2))
plt.imshow(mod, 'gray') #colormap ’binary’


T = np.random.normal(0, 1, 1024)
i2 = insertion(T,i2, 0.5)

plt.figure()
mod = np.log10(abs(i2))
plt.imshow(mod, 'gray') #colormap ’binary’


plt.show()