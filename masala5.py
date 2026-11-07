import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}

matn = json.dumps(talaba, indent=4)
print(matn)

yangi_talaba = json.loads(matn)

print("Ism:", yangi_talaba["ism"])