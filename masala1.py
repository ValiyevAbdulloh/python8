import json

with open("user.json", "r") as fayl:
    user = json.load(fayl)

print("Ism:", user["ism"])
print("Yosh:", user["yosh"])
print("Shahar:", user["shahar"])