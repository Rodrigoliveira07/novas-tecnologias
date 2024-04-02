pet1 = {
    "nome": "Bolinha",
    "tipo": "Cachorro",
    "dono": "Carlos"
}

pet2 = {
    "nome": "Miau",
    "tipo": "Gato",
    "dono": "Ana"
}

pet3 = {
    "nome": "Fifi",
    "tipo": "Papagaio",
    "dono": "Rafael"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Nome do animal: {pet['nome']}")
    print(f"Tipo do animal: {pet['tipo']}")
    print(f"Dono do animal: {pet['dono']}\n")