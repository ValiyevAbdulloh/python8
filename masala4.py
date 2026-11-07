import json

with open("phone.json", "r") as fayl:
    phone = json.load(fayl)

print("Model:", phone["model"])

yangi_narx = int(input("Yangi narxni kiriting: "))

phone["narx"] = yangi_narx

with open("phone.json", "w") as fayl:
    json.dump(phone, fayl, indent=4)

print("Narx yangilandi!")