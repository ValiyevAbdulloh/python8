import json

with open("product.json", "r") as fayl:
    product = json.load(fayl)

umumiy = product["narx"] * product["miqdor"]

print("Mahsulot:", product["nom"])
print("Umumiy qiymat:", umumiy, "so'm")