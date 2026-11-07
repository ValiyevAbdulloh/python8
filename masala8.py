import csv

ism = input("Ism: ")
yosh = input("Yosh: ")
kurs = input("Kurs: ")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([ism, yosh, kurs])

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)