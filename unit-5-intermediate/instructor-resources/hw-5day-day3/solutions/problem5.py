tv_characters = ["Will Byers", "Tyrion Lannister", "Oliver Queen", "Jean-Luc Picard", "Malcolm Reynolds", "The Doctor", "Sam Winchester", "Sherlock Holmes"]

# Open the file outside of the loop.
f = open("my_characters", "w")

for index, character in enumerate(tv_characters):
  f.write("{0}: {1}\n".format(index+1, character))

# This happens outside the loop, too.
f.close()
