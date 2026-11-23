'''
calculates ampltitudes of the 2p2h vectors to first order correction
It calculates for both perturbation expansion and configuration interaction expansion.
This is for later comparison.

The configuration interaction is intermediately normalised.

'''
import numpy as np

def Perturbation2p2hAmplitudes(g:float,i:int,a:int):
	'''
	g is the interaction coefficient
	i is specific hole state, i∈{1,2}
	a is specific particle state, a∈{3,4}
	'''

	k = g**2 / 16

	ei = 2*(i-1)
	ea = 2*(a-1)
	return k/(ei - ea)



