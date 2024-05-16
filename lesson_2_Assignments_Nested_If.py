#Nested Decisions: The Adventure Game
#Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    pass
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    pass

elif place == "cave":
    pass
    action = input("light a torch or proceed in the dark")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You are lost")
    pass
    
#2 Quick Decisions: The Event Planner
#Task 1: Code Correction
#Task 2: Venue Selection

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
food = input("Do you want vegetarian food?")
selection = "vegetarian" if food == "Yes" else "Gourmet Meals Caterers"
print(selection)