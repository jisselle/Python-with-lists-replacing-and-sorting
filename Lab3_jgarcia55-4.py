# Jisselle Garcia
# Lab3-4
# 01/28/23
# This program uses lists, append, replacing using specified index with a list, and removing from a list.

camping_list = [
    "tent",
    "cooler",
    "blankets",
    "pillows",
    "sleepings bags",
    "food",
    "water",
    "towels",
    "jacket",
    "hat",
]

camping_list.append("matches")
camping_list[9] = "binoculars"
camping_list.remove("binoculars")

print("Number of items in the car: ")
print(len(camping_list))

camping_list.sort()
print("The list includes: ")
print(camping_list)
