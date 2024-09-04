# List of Games
popularGames = ["Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
                 "Fortnite Battle Royale 39 Million 2017",
                 "Apex Legends 50 Million (1 Month) 2019",
                 "Leauge of Legends (LOL) 27 Million 2009",
                 "Counter Strike; Global Offensive 32 Million 2014",
                 "Heartstone 29 Million 20120",
                 "Minecraft 91 Million 2011",
                 "DOTA 2 5 million 2015",
                 "The Division 2 N/A 2019",
                 "The Splatoon 2"]

print(popularGames)
print()


# a]
print(f"5] {popularGames[4]}")
print(popularGames)
print()

# b]
dota_game = popularGames[7]
characters_in_name = len(dota_game)
print(f"The game {dota_game} has {characters_in_name} characters.")
print(popularGames)
print()

# c]
number_of_games = len(popularGames)
print(f"Er zitten {number_of_games} games in de lijst.")
print(popularGames)
print()

# d]
popularGames.insert(1, "Snake")
print(popularGames)
print()

# e]
index_of_splatoon = popularGames.index("The Splatoon 2")
splatoon = popularGames.pop(index_of_splatoon)
print(f"Helaas heeft de game {splatoon} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {splatoon}.")
print()

# f]
index_of_heartstone = popularGames.index("Heartstone 29 Million 20120")
popularGames[index_of_heartstone] = "Heartstone 29 Million 2012"
print(popularGames)
print()


# Tuple
computer_suppliers = ("Apple",
                      "Asus",
                      "Dell",
                      "Lenovo",
                      "Acer",
                      "Samsung",
                      "MSI",
                      "Hewlett-Packard (HP)",
                      "Toshiba",
                      "Microsoft",
                      "Chuwi",
                      "Sony")

print(computer_suppliers)
print()

# a]
number_of_computer_suppliers = len(computer_suppliers)
print(f"De tuple bevat {number_of_computer_suppliers} computer leveranciers.")

print(computer_suppliers)
print()

# b]
computer_supplier = computer_suppliers[7]
characters_in_name = len(computer_supplier)
print(f"De naam van {computer_supplier} bestaat uit {characters_in_name} karakters.")
print()

# c]
index_of_computer_supplier = computer_suppliers.index("Samsung")
print(f"De index van computer leverancier {computer_suppliers[index_of_computer_supplier]} is {index_of_computer_supplier}.")
print()