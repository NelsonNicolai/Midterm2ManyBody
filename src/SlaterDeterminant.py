import numpy as np
'''
The matrices here are as defined in question (5i)
for all functions g represents interaction coefficient
'''


def Wmat(g:float):#matrix
	#making unscaled matrix
	W = np.array([[0,1,1,0,1]
		,[1,0,0,1,1]
		,[1,0,0,1,1]
		,[0,1,1,0,1]
		,[1,1,1,1,0]])

	#scaling
	k = -g/2
	W = k*W

	return W

def Rmat(g:float):
	diag = np.array([-1,-1/2,-1/2,-1/3,-1/4])
	return np.diag(diag)


def wvec(g:float):#vector
	#unscaled vector
	w = np.array([1,1,1,1,0])

	#scaling
	k = -g / 2
	w = k*w

	return w