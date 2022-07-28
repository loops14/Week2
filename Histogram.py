#!/usr/bin/python3

import sys
import string
pip install matplotlib


#Used to split the list variables
l = list()
x = list.value()
k = list.key()

#Create a variable for the histogram

fig, plo = plt.subplots()

plo.hist(x)
plo.set_title('Total words') #Title
plo.set_xlabel(k) #Name of strings
plo.set_ylabel('Frequency') #Amount of words

plt.show() #Show graph