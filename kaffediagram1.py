#!/usr/bin/python3
import matplotlib, matplotlib.pyplot as plt, common, statistics, sys

def prepare_data1(filename):
    y_values = []
    x_values = []
    data = common.load_csv(filename)
    for index in range(len(data)):
        sum = 0
        if not(index == 0):
            y_values.append(statistics.mean(data[index][1:]))
            x_values.append(data[index][0])
    return [y_values,x_values]

def draw_diagram1(filename):
    y_values = prepare_data1(filename)[0]
    x_values = prepare_data1(filename)[1]
    plt.figure()
    plt.plot(x_values,y_values)
    plt.ylabel('antal koppar')
    plt.title("Koppar kaffe i snitt vid olika klockslag under en vecka")
    plt.savefig("antal_koppar.png")

def skapa_kaffediagram1(file):
    draw_diagram1(file)

if __name__ == "__main__":
    skapa_kaffediagram1(sys.argv[1])