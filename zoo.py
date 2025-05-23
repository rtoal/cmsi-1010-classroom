def show_help():
    print("Type 'help' to get a list of all the things you can do")
    print("Type 'see' to get a list of all the animals")
    print("Type 'help' to get a list of all the things you can do")
    print("Type 'pet' followed by the animal's name to pet a particular animal")
    print("Type 'bye' to leave the zoo and exit the program")


def show_all_animals():
    print("The animals in the zoo are:")
    print("• Clover the Bunny")
    print("• Coco the Mama Goat")
    print("• Arno the alligator")


def pet_animal(animal):
    if animal == "Clover":
        print("Clover is so happy!")
    elif animal == "Coco":
        print("Coco the Mama Goat thanks you!")
    elif animal == "Arno":
        print("Actually, we cannot allow you to pet Arno")
    else:
        print("I don't know that animal")


print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()

keep_going = True
while keep_going:
    response = input("What would you like to do? ")
    if response == "help":
        show_help()
    elif response == "see":
        show_all_animals()
    elif response.startswith("pet "):
        animal = response[4:]
        pet_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        keep_going = False
    else:
        print("Sorry, I don't understand that command.")
