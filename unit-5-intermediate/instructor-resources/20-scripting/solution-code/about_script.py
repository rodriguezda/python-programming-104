user_name = input("Please type your name: ")
user_food = input("Please type your favorite food: ")

file = open("about_me.txt", "w")
file.write("My name is " + user_name +  " and my favorite food is " +  user_food)
