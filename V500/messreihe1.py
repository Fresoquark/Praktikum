import numpy as np
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp

U,yel,red,gre,vio,uv = np.genfromtxt("data/messreihe1.csv",delimiter=",",unpack=True)

yel=np.sqrt(yel)
red=np.sqrt(red)
gre=np.sqrt(gre)
vio=np.sqrt(vio)
uv=np.sqrt(uv)

def f(x, a, b):
    return a*x+b

plt.figure(figsize=(4.76, 2.94))
plt.grid()
plt.xlabel(r"$U$ / $\si{\volt}$")
plt.ylabel(r'$\sqrt{I}$ / $\sqrt{\SI{100}{\pico\ampere}}$')


Uy = U[~np.isnan(yel)]
yel = yel[~np.isnan(yel)]
yelfit= np. delete(yel,[0,1,2,3,4,5,6,7,8,9])
Ufit= np. delete(Uy,[0,1,2,3,4,5,6,7,8,9])

params, covariance_matrix = curve_fit(f, Ufit, yelfit)
errors = np.sqrt(np.diag(covariance_matrix))

print('ay=', params[0], '+-', errors[0])
print('by=', params[1], '+-', errors[1])
ay=unp.uarray(params[0],errors[0])
by=unp.uarray(params[1],errors[1])
ny=(-by)/ay
print('ny=', ny)

plt.plot(Uy,yel, 'yellow',marker="x",linestyle="none", label="Daten (Gelb)", ms=2.5)
plt.plot(Ufit, f(Ufit, *params), 'yellow',linestyle="-", label='Fit (Gelb)')


Ur = U[~np.isnan(red)]
red = red[~np.isnan(red)]

params, covariance_matrix = curve_fit(f, Ur, red)
errors = np.sqrt(np.diag(covariance_matrix))

print('ar=', params[0], '+-', errors[0])
print('br=', params[1], '+-', errors[1])
ar=unp.uarray(params[0],errors[0])
br=unp.uarray(params[1],errors[1])
nr=(-br)/ar
print('nr=', nr)

plt.plot(Ur,red, 'rx', label="Daten (Rot)", ms=2.5)
plt.plot(Ur, f(Ur, *params), 'r-', label='Fit (Rot)')


Ug = U[~np.isnan(gre)]
gre = gre[~np.isnan(gre)]

params, covariance_matrix = curve_fit(f, Ug, gre)
errors = np.sqrt(np.diag(covariance_matrix))

print('ag=', params[0], '+-', errors[0])
print('bg=', params[1], '+-', errors[1])
ag=unp.uarray(params[0],errors[0])
bg=unp.uarray(params[1],errors[1])
ng=(-bg)/ag
print('ng=', ng)

plt.plot(Ug,gre, 'gx', label="Daten (Grün)", ms=2.5)
plt.plot(Ug, f(Ug, *params), 'g-', label='Fit (Grün)')

Uv = U[~np.isnan(vio)]
vio = vio[~np.isnan(vio)]

params, covariance_matrix = curve_fit(f, Uv, vio)
errors = np.sqrt(np.diag(covariance_matrix))

print('av=', params[0], '+-', errors[0])
print('bv=', params[1], '+-', errors[1])
av=unp.uarray(params[0],errors[0])
bv=unp.uarray(params[1],errors[1])
nv=(-bv)/av
print('nv=', nv)

plt.plot(Uv,vio, 'violet',marker="x",linestyle="none", label="Daten (Violett)", ms=2.5)
plt.plot(Uv, f(Uv, *params), 'violet',linestyle="-", label='Fit (Violett)')

Uu = U[~np.isnan(uv)]
uv = uv[~np.isnan(uv)]

params, covariance_matrix = curve_fit(f, Uu, uv)
errors = np.sqrt(np.diag(covariance_matrix))

print('au=', params[0], '+-', errors[0])
print('bu=', params[1], '+-', errors[1])
au=unp.uarray(params[0],errors[0])
bu=unp.uarray(params[1],errors[1])
nu=(-bu)/au
print('nu=', nu)

plt.plot(Uu,uv, 'darkviolet',marker="x",linestyle="none", label="Daten (Ultraviolett)", ms=2.5)
plt.plot(Uu, f(Uu, *params), 'darkviolet',linestyle="-", label='Fit (Ultraviolett)')




plt.legend(loc="upper center",ncol=5, fontsize=4.5)
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/messreihe1.pdf')
