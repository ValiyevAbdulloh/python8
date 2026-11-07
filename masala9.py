import csv

with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)

    xarajatlar = list(reader)

    jami = 0
    eng_katta = 0

    for x in xarajatlar:
        summa = int(x["summa"])
        jami += summa

        if summa > eng_katta:
            eng_katta = summa
            nom = x["nom"]

    print("Jami xarajat:", jami)
    print("Eng katta xarajat:", nom, eng_katta)
    print("Xarajatlar soni:", len(xarajatlar))