pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biriyani = ("Chicken Biriyani", "Indian", 45, "Hard")

print("Recipe 1: ", pasta)
print("Name: ", pasta[0])
print("Cuisine: ", pasta[1])
print("Cooking Time: ", pasta[2])
print("Difficulty: ", pasta[3])

print("Recipe 2: ", biriyani)
print("Name: ", biriyani[0])
print("Cuisine: ", biriyani[1])
print("Cooking Time: ", biriyani[2])
print("Difficulty: ", biriyani[3])

all_recipes = [pasta, biriyani]
print("\n First recipe name:", all_recipes[0][0])
print("Second recipe time:", all_recipes[1][2], "mins")
print("Pasta details (sliced)" , pasta[1:3])

print("\n Pasta recipe details:")
for detail in pasta:
    print("- ", detail)

print("\n Biriyani recipe details:")
for step in biriyani:
    print("- ", step)

