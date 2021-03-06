import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, cts, d = np.genfromtxt("data/aluminium.csv", delimiter=",", unpack=True)
ctserr=np.sqrt(cts)
print(ctserr)
cts=cts/t
ctserr=ctserr/t
d=d*1e-4
d=d*2.6989
null=568/900
nullerr=np.sqrt(568)/900
print(null,nullerr)
ctserr=ctserr-nullerr
cts=cts-null
print("Aktivität=",cts,"Fehler=",ctserr)
ctsfit1=np.delete(cts,[0,1,2,3,4])
dfit1=np.delete(d,[0,1,2,3,4])
ctsfit2=np.delete(cts,[5,6,7,8,9,10,11])
dfit2=np.delete(d,[5,6,7,8,9,10,11])


def f(x, a, b):
    return np.exp(a*x+b)


params, covariance_matrix = curve_fit(f,dfit1,ctsfit1,p0=(-110,0))
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a1=ufloat(params[0],errors[0])
b1=ufloat(params[1],errors[1])
schnittfit1=np.linspace(0,0.09)
plt.plot(schnittfit1, f(schnittfit1, *params), 'r-', label='Fit 1')

params, covariance_matrix = curve_fit(f,dfit2,ctsfit2,p0=(1.5,0))
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a2=ufloat(params[0],errors[0])
b2=ufloat(params[1],errors[1])
schnittfit2=np.linspace(0,0.14)
plt.plot(schnittfit2, f(schnittfit2, *params), 'b-', label='Fit 2')

rmax=(b2-b1)/(a1-a2)
print("Rmax=",rmax)
emax=1.92*unp.sqrt(rmax**2 + 0.22 * rmax)
print("Emax[MeV]= ",emax)
plt.yscale("log")
plt.errorbar(d, cts,yerr=ctserr,fmt='.k', label="Daten", ms=2.5)
plt.axvline(0.086,color="k",label="Rmax")
plt.legend(loc="best")
plt.grid()
plt.xlabel(r"R / $\si{\gram\per\centi\metre\squared}$")
plt.ylabel(r'$A_\text{total}$')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/aluminium.pdf')
