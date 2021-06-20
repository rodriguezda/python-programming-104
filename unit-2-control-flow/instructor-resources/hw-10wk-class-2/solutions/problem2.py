# If T-Rex is angry, hungry, and bored he will eat the Triceratops
# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon
# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
# Otherwise if T-Rex is tired, he goes to sleep
# Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
# Otherwise if T-Rex is angry or bored, he roars
# Otherwise T-Rex gives a toothy smile


angry = True
bored = True
hungry = False
tired = False

# Example if statement
if angry and hungry and bored:
  print("T-Rex eats the Triceratops!")
elif tired and hungry:
  print("T-Rex eats the Iguanadon")
elif hungry and bored:
  print("T-Rex eats the Stegasaurus")
elif tired:
  print("T-Rex goes to sleep.")
elif angry and bored:
  print("T-Rex fights with the Velociraptor")
elif angry or bored:
  print("T-Rex roars! RAWR!")
else:
  print("T-Rex gives a toothy smile.")
