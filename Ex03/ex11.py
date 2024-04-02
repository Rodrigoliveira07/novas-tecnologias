pessoa1 = {
    "first_name": "João",
    "last_name": "Silva",
    "age": 25,
    "city": "Rio de Janeiro"
}

pessoa2 = {
    "first_name": "Maria",
    "last_name": "Santos",
    "age": 30,
    "city": "São Paulo"
}

people = [pessoa1, pessoa2]

for pessoa in people:
    print(f"Nome completo: {pessoa['first_name']} {pessoa['last_name']}")
    print(f"Idade: {pessoa['age']} anos")
    print(f"Cidade: {pessoa['city']}\n")