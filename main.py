from math import log
from matplotlib import pyplot
from numpy import arange
from LoudspeakerDefinitions import l1

print("SPL Modeller")

# SPL = 20log(p/p0) where p0=20^-6
p0 = pow(20, -6)
p = 20
SPL = 20 * log(p / p0)

#print(SPL)

# L2 = L1 - |20log(r1/r2)|
def Calc_SPL_From_Distance(r, l_ref, r_ref):
    return l_ref - abs(20 * log(r_ref/r))

r_max = 250
l = []
for r in range(1, r_max):
    l.append(Calc_SPL_From_Distance(r, l1.SPL_max, 1))

x = arange(r_max-1)
pyplot.plot(l,x)
pyplot.title('L1')
pyplot.xlabel('SPL (dB)')
pyplot.ylabel('Distance (m)')
pyplot.show()