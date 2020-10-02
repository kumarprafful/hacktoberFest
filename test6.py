#!/usr/bin/env python

import sys

roman = str(arg[1])
l = len(roman)

val = {' ':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100}
sum = int(0)

flag = ''

for i in range(0,l-1):
	#print(roman[i],roman[i+1])
	if (val[roman[i]] < val[roman[i+1]]):
		sum = sum - val[roman[i]]
		
	if (val[roman[i]] == 0):
		flag = flag + chr(sum)
		sum = int(0)
		
	if(val[roman[i]] >= val[roman[i+1]]):
		sum = sum + val[roman[i]]
	print("Sum = ", sum)

print(flag)
