#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:52:24 2018

@author: 3874345
"""

import numpy as np
import matplotlib.pyplot as plt


def average(data, n):
    """ Moyenne les valeurs de data par paquets de taille n"""
    databis = data[len(data)%n:] # supprime les premiers éléments de data. Le nb d'éléments supprimés est le reste de la division euclidienne du nb d'éléments de data par n
    return databis.reshape(len(data)//n, n).mean(axis=1) # cree la matrice à len(data)//n colonnes et n lignes puis renvoie les moyennes de chaque ligne

data = np.arange(37)
n = 5
av = average(data,n)

def allan_variance_simple(data,n):
    data_average = average(data,n)
    data_diff = np.diff(data_average)
    data_squared = data_diff**2
    return np.mean(data_squared/2)

def allan_variance(data):
    Tn = 2**np.arange(int(np.log2(len(data)))-1)
    return Tn, np.array([allan_variance_simple(data, n) for n in Tn])

# Question 3

bruitBlanc = np.random.normal(size=1024)
Tn,var_Allan = allan_variance(bruitBlanc)

plt.loglog(Tn, var_Allan,'x')

# Question 4

marcheAleatoire = 0.1*np.cumsum(np.random.normal(size=2**16))
Tn,var_Allan = allan_variance(marcheAleatoire)

plt.loglog(Tn, var_Allan,'o')

# Question 5

sommeBruits = np.hstack((bruitBlanc,marcheAleatoire))
Tn,var_Allan = allan_variance(sommeBruits)

plt.loglog(Tn, var_Allan,'+')



# Température
data = np.loadtxt('temperature_londres.dat',delimiter=' ')

annees = data[:,0]
janvier = data[:,1]
avril = data[:,4]
juillet = data[:,7]
octobre = data[:,10]

plt.figure('Temperatures')
plt.plot(annees,janvier,label='janvier')
plt.plot(annees,avril,label='avril')
plt.plot(annees,juillet,label='juillet')
plt.plot(annees,octobre,label='octobre')
plt.legend()
plt.ylabel('Température (°C)')
plt.xlabel('Années')

plt.figure("Variances d'Allan des Temperatures")
Tn,var_Allan = allan_variance(janvier)
plt.loglog(Tn, var_Allan,label='janvier')

Tn,var_Allan = allan_variance(avril)
plt.loglog(Tn, var_Allan,label='avril')

Tn,var_Allan = allan_variance(juillet)
plt.loglog(Tn, var_Allan,label='juillet')

Tn,var_Allan = allan_variance(octobre)
plt.loglog(Tn, var_Allan,label='octobre')


# Bourse
ouvert = np.loadtxt('cac_40.csv',skiprows=4,delimiter=',',usecols=3,converters={3:eval})
plt.figure()
plt.plot(ouvert,label='ouverture')

Tn,var_Allan = allan_variance(ouvert)
plt.figure()
plt.loglog(Tn, var_Allan,label='ouverture')
