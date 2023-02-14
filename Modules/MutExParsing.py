#Run this code from terminal and pass arguments in the same line
# eg :   python ArgParse.py 2 3

#Add -h flag after name to get help

import math
import argparse

#instantiating parser
parser = argparse.ArgumentParser(description = 'Calculate volume of cylinder')

parser.add_argument('-r','--radius',metavar='',  type=int,required=True,help='Radius of cylinder')
parser.add_argument('-H','--height',metavar='',type=int,required=True,help='Height of cylinder')    

group = parser.add_mutually_exclusive_group() #sub of parser that we instantiated
group.add_argument('-q','--Quiet',action='store_true',help='print quiet')
group.add_argument('-v','--verbose',action='store_true',help='print verbose')

args = parser.parse_args()

def Cylinder_Volume(radius,height) :
    Vol = math.pi*radius*radius*height
    return Vol

vol = Cylinder_Volume(args.radius,args.height)

if(args.Quiet) :
    print(vol)
elif(args.verbose) :
    print('Vol of cyl with r=%s and h=%s is %s'%(args.radius,args.height,vol))
else :
    print('vol = %s'%(vol))


