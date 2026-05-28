pasta_ingredients = {"Pasta", "Tomato", "Garlic", "Olive Oil"}
biriyani_ingredients = {"Rice", "Chicken", "Spices", "Yogurt", "Tomato"}

print("\nPasta Ingredients: ", pasta_ingredients)
print("Biriyani Ingredients: ", biriyani_ingredients)
print("Total pasta ingredients: ", len(pasta_ingredients))
print("Total biriyani ingredients: ", len(biriyani_ingredients))

pasta_ingredients.add("Parmesan")
pasta_ingredients.discard("Garlic")
print("\nUpdated Pasta Ingredients: ", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biriyani_ingredients)
common = pasta_ingredients.intersection(biriyani_ingredients)
onlt_pasta = pasta_ingredients.difference(biriyani_ingredients)
unique_ingredients = pasta_ingredients.symmetric_difference(biriyani_ingredients)

print("\nAll Ingredients(union): ", all_ingredients)
print("Common Ingredients(intersection): ", common)
print("Only Pasta Ingredients(difference): ", onlt_pasta)
print("Unique Ingredients(symmetric difference): ", unique_ingredients)

