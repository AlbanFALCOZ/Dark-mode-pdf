# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:38:03 2023

@author: alban
"""



# import module
import sys
import os
from PIL import Image
from pdf2image import convert_from_path
from pypdf import PdfMerger
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('UNE ÉTUDE EN ROUGE.pdf',poppler_path=r"C:\Users\alban\OneDrive\Documents\Informatique\Python\library\poppler-23.11.0\Library\bin")



def reversed_color(im):
    newimdata = []
    for color in im.getdata():
        newimdata.append(((255-color[0],255-color[0],255-color[0])))
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim


def createEachPage(images):
    listNameImage = []
    for i in range(len(images)):
        print("Page numéro : " + str(i))
        nameImage = 'page'+ str(i) +'.pdf'
        listNameImage.append(nameImage)
        try :
            reversed_color(images[i]).save(nameImage)
        except FileNotFoundError as e :
            print("Error : " + e.filename + " - " + e.strerror)
            print("This error occurs if the specified file path doesn't exist. Make sure the directory structure is correct or create the directories if needed")
        except PermissionError as e:
            print("Error : " + e.filename + " - " + e.strerror)
            print("You may encounter this error if you don't have the necessary permissions to write to the specified file or directory. Ensure that your script has write permissions")
        except IOError as e :
            print("Error : " + e.filename + " - " + e.strerror)
            print("These errors can occur for various reasons, such as a file being open in another process or if the file is in use. Make sure the file is not being accessed by another program")
        
    mergePdfTogether(listNameImage)
    

def mergePdfTogether(listNameImage):
    merger = PdfMerger()
    for image in listNameImage :
        try :
            merger.append(image)
        except FileNotFoundError as e :
            print("Error : " + e.filename + " - " + e.strerror)
            print("This error occurs if the specified file path doesn't exist. Make sure the directory structure is correct or create the directories if needed")
    try :
        merger.write("darkMode.pdf")
    except FileNotFoundError as e :
        print("Error : " + e.filename + " - " + e.strerror)
        print("This error occurs if the specified file path doesn't exist. Make sure the directory structure is correct or create the directories if needed")
    merger.close()
    
    deleteAllSingleFile(listNameImage)
    
def deleteAllSingleFile(listNameImage):
    for image in listNameImage :   
        try :
            os.remove(image)
        except OSError as e :
            print("Error : " + e.filename + " - " + e.strerror)
    
createEachPage(images)
