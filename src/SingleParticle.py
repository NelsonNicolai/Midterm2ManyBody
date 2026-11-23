import numpy as np

'''
The relevant equations for the single particle basis for problem 6 in midterm

g is the interaction coefficient of the pairing model
'''

def Wpphh(g:float):
	k = -g/2
	Wpphh = np.array([[1,1],[1,1]])
	return k*Wpphh

def T(g:float):
	k = -g/2
	T = np.array([[-1/4,-1/2],[-1/6,-1/4]])
	return k*T

