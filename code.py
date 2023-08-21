import matplotlib.pyplot as plt
import numpy as np

ASiO2 = np.array([0.6961663,0.4079426,0.8974794])
BSiO2 = np.array([0.0684043,0.1162414,9.896161])
AMgF2 = np.array([0.48755108,0.39875031,2.3120353])
BMgF2 = np.array([0.04338408,0.09461442,23.793604])
L = np.linspace(0.4,1,100)

#Refractive index of SiO2
n1SiO2 = (ASiO2[0]*L**2)/(L**2-BSiO2[0]**2)
n2SiO2 = (ASiO2[1]*L**2)/(L**2-BSiO2[1]**2)
n3SiO2 = (ASiO2[2]*L**2)/(L**2-BSiO2[2]**2)
nSiO2 = n1SiO2+n2SiO2+n3SiO2
square_n_SiO2 = 1 + nSiO2
n_SiO2 = np.sqrt(square_n_SiO2)

#Refractive index of MgF2
n1MgF2 = (AMgF2[0]*L**2)/(L**2-BMgF2[0]**2)
n2MgF2 = (AMgF2[1]*L**2)/(L**2-BMgF2[1]**2)
n3MgF2 = (AMgF2[2]*L**2)/(L**2-BMgF2[2]**2)
nMgF2 = n1MgF2+n2MgF2+n3MgF2
square_n_MgF2 = 1 + nMgF2
n_MgF2 = np.sqrt(square_n_MgF2)

plt.plot(L,n_SiO2,'-b', label='SiO2')
plt.plot(L,n_MgF2, '-k', label='MgF2')
plt.xlabel('Wavelength')
plt.ylabel('Refractive Index')
plt.legend()
