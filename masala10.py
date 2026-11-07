import csv

with open("sportchilar.csv", "r") as file:
    reader = csv.DictReader(file)

    sportchilar = list(reader)

    eng_yuqori = 0

    for s in sportchilar:
        ball = int(s["ball"])

        print(s["ism"], s["sport"], ball)

        if ball > 80:
            print("80 dan yuqori:", s["ism"])

        if ball > eng_yuqori:
            eng_yuqori = ball
            ism = s["ism"]

    print("Eng yuqori ball:", ism, eng_yuqori)