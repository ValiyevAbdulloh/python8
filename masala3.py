import json

with open("student.json", "r") as fayl:
    student = json.load(fayl)

student["ball"] = 95

with open("student.json", "w") as fayl:
    json.dump(student, fayl, indent=4)

print(student)