import csv


import csv

def load_csv(filename):
    with open(filename) as file:
        data = csv.reader(file)
        lst_of_data1 = []
        lst_of_data2 = []
        for row in data:
            lst_of_data1.append(row)
        for index in range(len(lst_of_data1)):
            if index == 0:
                lst_of_data2.append([lst_of_data1[index][0].split(";")])
            else:
                lst_of_data2.append(list(map(int, lst_of_data1[index][0].split(";"))))
    return lst_of_data2