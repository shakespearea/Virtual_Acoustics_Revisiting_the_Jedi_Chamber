from math import log
from matplotlib import pyplot
from numpy import arange, array, pi, sin, linspace, log10
from LoudspeakerDefinitions import l1

print("SPL Modeller")

# L2 = L1 - |20log(r1/r2)|
def Calc_SPL_From_Distance(r, l_ref, r_ref):
    return l_ref - abs(20 * log(r_ref/r))

r_max = 250
l = []
for r in range(1, r_max):
    l.append(Calc_SPL_From_Distance(r, l1.SPL_max, 1))

# x = arange(r_max-1)
# pyplot.plot(l,x)
# pyplot.title('L1')
# pyplot.xlabel('SPL (dB)')
# pyplot.ylabel('Distance (m)')
# pyplot.show()

# λ = c/ω, where c=343
# Horizontal directivity k = 2π/λ
# ka = ka/2
# Directivity = |sin(ka sinθ)/ka sinθ|
def Calc_Directivity(angle, frequency, width):
    c = 343
    wavelength = c/frequency
    k = 2 * pi / wavelength
    ka = k * width / 2
    kaSin = ka*sin(angle)
    if abs(kaSin) < 1e-10:
        return 1.0
    return abs(sin(kaSin)/kaSin) 

directivity = []
angles = []
resolution = 1000
frequency = 5000
for theta in linspace(-pi, pi, resolution):
    angles.append(theta)
    directivity.append(Calc_Directivity(theta, frequency, l1.d.w/1000))

# SPL = 20log(Dθ)
SPL = 20 * log10(array(directivity))

pyplot.figure()
polarPlot = pyplot.subplot(111, projection='polar')
polarPlot.plot(angles,SPL)
polarPlot = pyplot.title('L1 Directivity at 1000 Hz')
pyplot.show()