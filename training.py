potion = {
    "name":                          "potion of strength",
    "level":                         2, 
    "buff":                         "gives x2 damage",
    "multiplier":                    2,
}
for ky in potion:
    print(f"Key: {potion[ky]}")
    print(ky)
print(random.random())
if random.random()>0.15:
    print("banaan")