import csv
dataset_1=[]
dataset_2=[]

with open("Star.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("Dwarf1.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

h1 = dataset_1[0]
h2 = dataset_2[0]

sd1 = dataset_1[1:]
sd2 = dataset_2[1:]

h = [h1+h2]
sd = []

for i in sd1:
    sd.append(i)

for i in sd2:
    sd.append(i)

with open("Final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(sd)
