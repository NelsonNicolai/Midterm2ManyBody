from src import SlaterDeterminant as slater
import numpy as np
import matplotlib.pyplot as plt
from src import SingleParticle
'''
1st order wave operator and configuration interaction 2p2h state amplitudes
'''




'''
Slater Determinants

E(2) is given by <WRW>
E(3) is given by <WRWRW>
<> implies two ground states on either sides
w vector is the action of W onto the ground state
We note that W is hermitian

the iteration makes the energy values as a list where each respective term shares same g value
'''

#making the g values
glist = np.linspace(start = -1, stop = 1, endpoint = True,num = 50)

Ec1 = []
Ec2 = []
Ec3 = []

for g in glist:
	W = slater.Wmat(g)
	R = slater.Rmat(g)
	w = slater.wvec(g)


	Ec1.append(g)
	Ec2.append(w.transpose()@R@w)
	Ec3.append(w.transpose()@R@W@R@w)

Ec1 = np.array(Ec1)
Ec2 = np.array(Ec2)
Ec3 = np.array(Ec3)

#0th order correction is constant with respect to g
Ec0 = np.ones(len(Ec1))*2


'''
graphs of slater determinants
'''
folder = "report/Diagrams/" #path

#Third order
plt.plot(glist,Ec3)
plt.title("Third order Error Correction")
plt.xlabel("Interaction Strength (g)")
plt.ylabel("Energy correction ($E^{(3)}$)")
plt.savefig(folder + "SlaterEu3.png")
plt.close()

#Second order
plt.plot(glist,Ec2)
plt.title("Second order Error Correction")
plt.xlabel("Interaction Strength (g)")
plt.ylabel("Energy correction ($E^{(2)}$)")
plt.savefig(folder + "SlaterEu2.png")
plt.close()

#First order
plt.plot(glist,Ec1)
plt.title("First order Error Correction")
plt.xlabel("Interaction Strength (g)")
plt.ylabel("Energy correction ($E^{(1)}$)")
plt.savefig(folder + "SlaterEu1.png")
plt.close()

#energy
E = Ec0 + Ec1 + Ec2 + Ec3 #sum of all corrections

plt.plot(glist,E)
plt.title("Energy to third Order")
plt.xlabel("Interaction Strength (g)")
plt.ylabel("Energy (E)")
plt.savefig(folder + "SlaterE.png")
plt.close()


'''
Single particle basis
'''

Ec2_SB = []

for g in glist:	
	Wpphh = SingleParticle.Wpphh(g)
	T     = SingleParticle.T(g)
	Ec2_SB.append(0.25 * np.sum(np.diag(Wpphh@T)))


'''
graphs of Single Particle Basis
'''

plt.plot(glist,Ec2_SB)
plt.title("First order Error Correction")
plt.xlabel("Interaction Strength (g)")
plt.ylabel("Energy correction ($E^{(1)}$)")
plt.savefig(folder + "SBEu2.png")
plt.close()