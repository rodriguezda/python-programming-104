# Fixed Code (You may have some small variations!)
rainbow = {
  "name": "Roy G. Biv",
  "colors": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
  "end": "Pot of gold!",
  "number": "double",
  "count": 2,
  "gold": 100
}

print("The rainbow's name is", rainbow["name"])

if rainbow["end"] == "Pot of gold!":
    print("I'll be taking that gold!")
else:
  print("No money for me!")

for color in rainbow["colors"]:
  if color is not "indigo":
    print(color)
  else:
    print("What color is indigo?")

gold_amount = rainbow["count"] + rainbow["gold"]
print(gold_amount)

persons = 1
split_gold = rainbow["gold"] / persons
print(split_gold)
