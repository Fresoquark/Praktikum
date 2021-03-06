import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x,I = np.genfromtxt("data/ds2.csv",delimiter = ",", unpack=True)

x = x-25 #Zentrieren der Werte
I = I-0.021 #Subtraktion des Dunkelstromes
xbla= np.linspace(-15,15, 1000) #Weicherer Fit
lada = 635 * 10**(-6) #Wellenlänge Lambda in Millimeter
L = 99.5 * 10 #Länge L in Millimeter


def f(x, a, b, c, d, e):
    #return a**2 * b**2 * (lada /( np.pi * b * np.sin(x/(L) + c )))**2 * np.sin(np.pi * b * np.sin(x /(L) + c ) / (lada))
    return  a**2 * np.sinc(np.pi * b * np.sin(x/L+c)/(lada))**2 * 4 * np.cos( (e * np.pi * np.sin(x/L+c)) / (lada) )**2 + d

params, covariance_matrix = curve_fit(f, x, I, p0=(2.2, 0.15, 0, 2, 0.5))

errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
print('c=', params[2], '+-', errors[2])
print('d=', params[3], '+-', errors[3])
print('e=', params[4], '+-', errors[4])


plt.plot(x, I, 'k.', label="Daten", ms=2.5)
plt.plot(xbla, f(xbla, *params), 'r--', label='Fit')


plt.xlabel(r'Position /$\si{\milli\metre}$ ')
plt.ylabel(r'Photostrom/$\si{\micro\ampere}$')
plt.legend(loc='best')
plt.grid()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/ds2.pdf')
