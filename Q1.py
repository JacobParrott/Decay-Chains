import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import scipy as sci
from scipy.integrate import odeint

'''
Edit this function as part of Activity 1B
This function should accept the a filename of a file in the endf dataset and return its decay rate and decay mode
:param filename: str containing the filename to be read from, with no path prefix (such as "dec-019_K_040.endf")
:returns: Should be a tuple containing the decay rate as a float units of 1/s, and the change to the atomic number and atomic mass caused by the decay as ints (e.g. (1.0, -2, 4) for alpha decay with a decay rate of 1.0/s)
'''
#find half-life value in file


#document the below function
#this function should accept the filename of a file in the
# 1. read the file
# 2. find the half-life value
# 3. find the decay mode
# 4. return the half-life value and decay modes


# how could I make the code more efficient?
# you could use a for loop to iterate through the lines of the file


def get_decay_rate(filename):
    #open file
    file = open(filename, "r")
    #read file
    file = file.readlines()
    #find half-life and decay mode
    for line in file:
        if "Parent half-life" in line:
            #split line after ':'

            l = line.split(":")[1]
            #print this before Y
            #line = line.split("")[0]
            #remove the first space
            l = l[1:]

            #extract the first number
            l = l.split(" ")[0]
            #convert to float
            l = float(l)
            #get half-life value
            half_life = l
            
            #this is in years, convert to seconds
            half_life = half_life * 365 * 24 * 60 * 60
            #get decay rate
            decay_rate = np.log(2)/half_life

 
        #find decay mode
        if 'Decay Mode' in line:
        #split line after ':'
            line = line.split(":")[1]
            #print this before Y
            #line = line.split("")[0]
            #remove the first space
            line = line[1:]

            #extract the first number
            v = line.split(" ")[0]
            #if v is B, return [+1, 0]; if v is A, return [-2, -4], if v is E, return [-1, 0], else return [0,0]
            if v == 'B-':
                return (decay_rate, +1, 0)
            elif v == 'A':
                return (decay_rate, -2, -4)
            elif v == 'E':
                return (decay_rate, -1, 0)
            else:
                return (decay_rate, 0, 0)
    
            
            




    
    #calculate change in atomic number and mass

def MakeFileName(atomicNumber, element, atomicMass,EnergyState):
    '''make a string the starts with ''dec-'', "atomicNumber" in 3 sig fig, element letter,
    "AtomicNumber" in 3 sig fig, "m", "EnergyState", end with ends with ''.endf''
    '''
    #convert atomic number to string
    atomicNumber = str(atomicNumber)
    #element letter
    element = str(element)
    #convert atomic mass to string of length 3
    atomicMass = str(atomicMass)
    #if length of atomic mass is 1, add 2 zeros
    if len(atomicMass) == 1:
        atomicMass = '00' + atomicMass
    #if length of atomic mass is 2, add 1 zero
    elif len(atomicMass) == 2:
        atomicMass = '0' + atomicMass

    #do the same for atomic number
    if len(atomicNumber) == 1:
        atomicNumber = '00' + atomicNumber
    elif len(atomicNumber) == 2:
        atomicNumber = '0' + atomicNumber

    #q: what is an energy state?
    #a: the energy state of a nucleus is the energy of the nucleus in its ground state




    

    
    #convert energy state to string
    EnergyState = str(EnergyState)
    #return string
    filename = 'dec-' + atomicNumber + '_' + element + '_' + atomicMass + 'm' + EnergyState + '.endf'
   
    #return string
    return filename



print(MakeFileName(8,'O',16,2))
dr, atomicNumber, atomicMass = get_decay_rate('decay_data/dec-002_He_006.endf')
print(dr, atomicNumber, atomicMass)

# Q: what does the python package periodictable do? 
# A: it is a python package that contains information about the elements of the periodic table
#Q: what are some of its functions?
#A: it can return the atomic number, atomic mass, and name of an element given its symbol
#Q: what are the install instructions for this?
#A: pip install periodictable
