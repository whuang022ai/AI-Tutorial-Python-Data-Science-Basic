
# -*- coding: UTF-8 -*-

def reverse_string():
	str = input('Please input string to reverse :')
	rever = [None]*len(str)
	for i in range (len(str)):
		rever[len(str)-i-1] = str[i]
	return rever
	
restr=''.join(reverse_string())
print('Reverse the string:',restr)
