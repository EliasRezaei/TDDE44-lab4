#!/usr/bin/python3
import matplotlib, matplotlib.pyplot as plt, common, sys

def prepare_data2(filename):
    values = []
    data = common.load_csv(filename) 
    for index1 in range(8):
        sum = 0
        if not(index1 == 0):
            for index2 in range(len(data)):
                if not(index2 == 0):
                    sum += data[index2][index1]
            values.append(sum)
    return values

def draw_diagram2(filename):
    y_values = prepare_data2(filename)
    x_values = common.load_csv(sys.argv[1])[0][0][1:]
    plt.plot(x_values,y_values)
    plt.ylabel('antal koppar')
    plt.title("Koppar kaffe per dag")
    

def skapa_kaffediagram2(filename):
    plt.figure()
    draw_diagram2(filename)
    plt.savefig("antal_koppar.png")

if __name__ == "__main__":
    skapa_kaffediagram2(sys.argv[1])