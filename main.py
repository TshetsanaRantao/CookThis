import csv

import requests
import json

from pprint import pprint

print("\nWelcome to Cook This, your holistic meal finder!")

print("\nPlease fill in your details below to get cooking!")

print("\n")

name = input("Name: ")
surname = input("Surname: ")

ingredient_one = input(
  "Please enter the first ingredient you'd like to cook with ")
ingredient_two = input(
  "Please enter the second ingredient you'd like to cook with ")
ingredient_three = input(
  "Please enter the third ingredient you'd like to cook with ")

while True:
  vegan = input("Would you like vegan options? yes/no ")
  if vegan == 'yes':
    break
  elif vegan == 'no':
    break
  else:
    print("Sorry, please can you answer 'yes'       or 'no'")
    continue

while True:
  vegetarian = input("Would you like vegetarian options? yes/no ")
  if vegetarian == 'yes':
    break
  elif vegetarian == 'no':
    break
  else:
    print("Sorry, please can you answer 'yes'       or 'no'")
    continue

while True:
  high_protein = input("Would you like high protein options? yes/no ")
  if high_protein == 'yes':
    break
  elif high_protein == 'no':
    break
  else:
    print("Sorry, please can you answer 'yes'       or 'no'")
    continue

while True:
  low_fat = input("Would you like low-fat options? yes/no ")
  if low_fat == 'yes':
    break
  elif low_fat == 'no':
    break
  else:
    print("Sorry, please can you answer 'yes'       or 'no'")
    continue

while True:
  gluten_free = input("Would you like gluten-free options? yes/no ")
  if gluten_free == 'yes':
    break
  elif gluten_free == 'no':
    break
  else:
    print("Sorry, please can you answer 'yes'       or 'no'")
    continue

while True:
  peanut_free = input("Would you like peanut-free options? yes/no ")
  if peanut_free == 'yes':
    break
  elif peanut_free == 'no':
    break
  else:
    print("Sorry, please can you answer 'yes'       or 'no'")
    continue

while True:
  dairy_free = input("Would you like dairy-free options? yes/no ")
  if dairy_free == 'yes':
    break
  elif dairy_free == 'no':
    break
  else:
    print("Sorry, please can you answer 'yes'       or 'no'")
    continue


def get_ingredient_one(ingredient_one):
  return f"&q={ingredient_one}"


def get_ingredient_two(ingredient_two):
  return f"&q={ingredient_two}"


def get_ingredient_three(ingredient_three):
  return f"&q={ingredient_three}"


def is_vegan(vegan):
  if vegan == "yes":
    return "&health=vegan"
  else:
    return ""


def is_vegetarian(vegetarian):
  if vegetarian == "yes":
    return "&health=vegetarian"
  else:
    return ""


def is_high_protein(high_protein):
  if high_protein == "yes":
    return "&diet=high-protein"
  else:
    return ""


def is_low_fat(low_fat):
  if low_fat == "yes":
    return "&diet=low-fat"
  else:
    return ""


def is_gluten_free(gluten_free):
  if gluten_free == "yes":
    return "&health=gluten-free"
  else:
    return ""


def is_dairy_free(dairy_free):
  if dairy_free == "yes":
    return "&health=dairy-free"
  else:
    return ""


def is_peanut_free(peanut_free):
  if peanut_free == "yes":
    return "&health=peanut-free"
  else:
    return ""


apiKey = '1ee6254fcc65b726786703ec86a9b87e'
apiId = '1c88cb7f'

ingredients = []
diet = []
allergens = []
health = []

url = 'https://api.edamam.com/api/recipes/v2?type=public'
url2 = f'{get_ingredient_one(ingredient_one)}{get_ingredient_two(ingredient_two)}{get_ingredient_three(ingredient_three)}{is_vegan(vegan)}{is_low_fat(low_fat)}{is_vegetarian(vegetarian)}{is_gluten_free(gluten_free)}{is_high_protein(high_protein)}{is_peanut_free(peanut_free)}{is_dairy_free(dairy_free)}&app_id={apiId}&app_key={apiKey}'

fullUrl = url + url2

body = requests.get(fullUrl)
json = json.loads(body.text)

results = json['hits']

allRecipes = results
listOfRecipes = []
listOfRecipeLabels = []

for i in allRecipes:
  listOfRecipes.append(i['recipe'])

for i in listOfRecipes:
  listOfRecipeLabels.append(i['label'])

field_names = [
  'first_name', 'surname', 'vegan_options', 'vegetarian_options',
  'high_protein_options', 'low_fat_options', 'gluten_free_options',
  'dairy_free_options', 'peanut_free_options'
]

dataInput = {
  'first_name': name,
  'surname': surname,
  'vegan_options': vegan,
  'vegetarian_options': vegetarian,
  'high_protein_options': high_protein,
  'low_fat_options': low_fat,
  'gluten_free_options': gluten_free,
  'dairy_free_options': dairy_free,
  'peanut_free_options': peanut_free,
  
}

with open('recipe.csv', 'w+') as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=field_names)
  writer.writeheader()
  writer.writerow(dataInput)

with open('recipe.csv', 'a', newline='') as csvfile:
  spamwriter = csv.writer(csvfile)
  for i in listOfRecipeLabels:
    spamwriter.writerow([i])

print("\nYour recipe options are available in the recipe.csv file")

print("\nThank you for using Cook This!")
