#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Sample zum Plotten eines Graphen
#
# Installation: http://matplotlib.org/users/installing.html
# Unter Linux war noch folgendes notwendig:
#     apt-get install python3-matplotlib
#     apt-get install python3-tk
#
# Auf MAC
#	python3 -m pip install matplotlib
#

import matplotlib.pyplot as plt


def simple_plot(label, values):
    plt.plot(values)
    plt.ylabel(label)
    plt.show()

simple_plot("Mein Label",[1,2,3,4])
