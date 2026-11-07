import csv

with open("products.csv", "r") as file:
    reader = csv.DictReader(file)

    mahsulotlar = list(reader)

    eng_qimmat = 0

    for m in mahsulotlar:
        nom = m["nom"]
        narx = int(m["narx"])
        miqdor = int(m["miqdor"])

        jami = narx * miqdor

        print(nom, narx, miqdor, "Umumiy:", jami)

        if narx > eng_qimmat:
            eng_qimmat = narx
            qimmat_mahsulot = nom

    print("Eng qimmat mahsulot:", qimmat_mahsulot)