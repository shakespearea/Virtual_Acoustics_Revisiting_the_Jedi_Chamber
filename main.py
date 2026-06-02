from math import log
from matplotlib import pyplot, cm
from numpy import arange, array, pi, sin, linspace, log10, random
from LoudspeakerDefinitions import l1

print("Loudspeaker Modeller")

# L2 = L1 - |20log(r1/r2)|
def Calc_SPL_From_Distance(r, l_ref, r_ref):
    return l_ref - abs(20 * log(r_ref/r))

r_max = 250
l = []
for r in range(1, r_max):
    l.append(Calc_SPL_From_Distance(r, l1.SPL_max, 1))

x = arange(r_max-1)
pyplot.plot(l,x)
pyplot.title('L1 SPL over 250m')
pyplot.xlabel('SPL (dB)')
pyplot.ylabel('Distance (m)')
#pyplot.show()

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

resolution = 1000
frequencies = l1.bw.min + arange(l1.bw.max - l1.bw.min)
colours = pyplot.cm.viridis(linspace(0,1,max(frequencies)+1))
pyplot.figure()
polarPlot = pyplot.subplot(111, projection='polar')
for f in frequencies:
    directivity = []
    angles = []
    for theta in linspace(-pi, pi, resolution):
        angles.append(theta)
        directivity.append(Calc_Directivity(theta, f, l1.d.w/1000))
    # SPL = 20log(Dθ)
    SPL = 20 * log10(array(directivity))
    polarPlot.plot(angles,SPL, color=colours[f])
polarPlot = pyplot.title('L1 Directivity at 1000 Hz')
pyplot.show()