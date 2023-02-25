#!/usr/bin/python3
import matplotlib, matplotlib.pyplot as plt, sys, kaffediagram2 as k2

def skapa_kaffediagram3():
    file_list = sys.argv[1:]
    plt.figure()
    for file in file_list:
        k2.draw_diagram2(file)
    plt.savefig("antal_koppar.png")

skapa_kaffediagram3()