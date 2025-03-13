students = [
    {"name": "hermioni", "house": "gryffindor", "patronus": "otter"},
    {"name": "harry", "house": "gryffindor", "patronus": "stag"},
    {"name": "ron", "house": "gryffindor", "patronus": "jack russell terrier"},
    {"name": "draco", "house": "slytherin", "patronus": None},
 ]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ", end=".\n")
