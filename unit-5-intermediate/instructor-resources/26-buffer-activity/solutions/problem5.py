def letter_counter(input):
    counts = {}
    for char in input:
        if char in counts:
            # If the key already exists, we just add to the existing count
            counts[char] += 1
        else:
            # If we don't find the key, we'll add it and assign a count of 1
            counts[char] = 1

    # Remember to return OUTSIDE the for loop!
    return counts




# Uncomment the code below if you want to test out the example code

# word_to_count = "banana"
# result = letter_counter(word_to_count)
# print(result)
