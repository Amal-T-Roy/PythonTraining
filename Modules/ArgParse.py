#Run this code from terminal and pass arguments in the same line
# eg :   python ArgParse.py 2 3

#Add -h flag after name to get help

import math
import argparse

parser = argparse.ArgumentParser(description = 'Calculate volume of cylinder')
parser.add_argument('radius',type=int,help='Radius of cylinder')
parser.add_argument('height',type=int,help='Height of cylinder')    

args = parser.parse_args()


def Cylinder_Volume(radius,height) :
    Vol = math.pi*radius*radius*height
    return Vol

print(Cylinder_Volume(args.radius,args.height))