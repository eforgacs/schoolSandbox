married_partners = {"Sejin": "Eddie", "Jacquie": "Eva", "Kyung Ok": "Heung Ki"}

# print(married_partners["Sejin"])


def insert(table, key, value):
    table[key] = value


animals = {"birds": ["pigeon", "eagle", "cuckoo"], "fish": ["salmon", "tuna", "yellowtail"]}

insert(animals, "birds", "owl")

print(animals["birds"])
