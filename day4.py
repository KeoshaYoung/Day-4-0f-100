print("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")

name = input("What is your name?")
enemy = input("What is your worst enemy's name?")
superpower = input("What is your superpower?")
location = input("Where do you live?")
food = input("What is your favorite food?")

print("Hello", name, "! Your ability to", superpower, "will make sure you never have to look at", enemy,
      "again. Go eat", food, "as you walk down the streets of", location, "and use", superpower, "for\033[32m good\033[0m and not\033[31m evil!\033[0m")
