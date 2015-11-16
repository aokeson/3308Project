#!/bin/bash/

from pyPdf import PdfFileReader

f=open('https://housing.colorado.edu/sites/default/files/menus/dining_menu.pdf', 'rb')
reader=PdfFileReader(f)
contents=reader.getpage(0).extractText().split('  ')
f.close()
