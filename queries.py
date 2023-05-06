from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

pikachu = pokemonColl.find_one({"name" : "Pikachu"})
print(pikachu['name'])
print("-----------------------")

greater_than = pokemonColl.find({"attack" : { "$gt": 150 }})
for pokemon in greater_than:
    print(pokemon['name']) 
print("-----------------------")

ability_overgrow = pokemonColl.find({ "abilities" : { "$regex" : "Overgrow" }})
for pokemon in ability_overgrow:
    print(pokemon['name'])
