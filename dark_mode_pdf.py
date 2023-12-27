# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:38:03 2023

@author: alban
"""

from PIL import Image
from pdf2image import convert_from_path
from random import *

imagePath = 'cat.jpg'
#pil_image_lst = convert_from_path(imagePath,poppler_path=r'C:\Users\alban\OneDrive\Documents\Informatique\Python\library\poppler-23.11.0\Library\bin') # This returns a list even for a 1 page pdf
#pil_image = pil_image_lst[0]
newImagePath = 'darkmode.jpg'
im = Image.open(imagePath)
#im = Image.open(pil_image)



def redOrBlack (im):
    comptPixel = 0
    comptRedPixel = 0
    newimdata = []
    redcolor = (255,0,0)
    blackcolor = (0,0,0)
    for color in im.getdata():
        if color >= (255,0,0)  :
            newimdata.append( redcolor )
            #print(newimdata[0],newimdata[1],newimdata[2])
            #comptRedPixel = comptRedPixel+1
            #print(comptRedPixel)
        else:
            newimdata.append( ((255-color[0],255-color[0],255-color[0])) )
            #newimdata.append( (randint(0,255),randint(0,255),randint(0,255)) )
        #comptPixel = comptPixel +1
        #print(comptPixel)
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

redOrBlack(im).save(newImagePath)