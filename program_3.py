# Eliya Statema
# 3/21/25
# Capital Quiz

import random

print("This program will quiz your knowledge of the capitals of the 50 states.")

def main():
    state_capitals = {
        "Alabama" : "Montgomery",
        "Alaska" : "Juneau",
        "Arizona" : "Phoenix",
        "Arkansas" : "Little Rock",
        "California" : "Sacramento",
        "Colorado" : "Denver",
        "Connecticut" : "Hartford",
        "Delaware" : "Dover",
        "Florida" : "Tallahassee",
        "Georgia" : "Atlanta",
        "Hawaii" : "Honolulu",
        "Idaho" : "Boise",
        "Illinois" : "Springfield",
        "Indiana" : "Indianapolis",
        "Iowa" : "Des Moines",
        "Kansas" : "Topeka",
        "Kentucky" : "Frankfort",
        "Louisiana" : "Baton Rouge",
        "Maine" : "Augusta",
        "Maryland" : "Annapolis",
        "Massachusetts" : "Boston",
        "Michigan" : "Lansing",
        "Minnesota" : "Saint Paul",
        "Mississippi" : "Jackson",
        "Missouri" : "Jefferson City",
        "Montana" : "Helena",
        "Nebraska" : "Lincoln",
        "Nevada" : "Carson City",
        "New Hampshire" : "Concord",
        "New Jersey" : "Trenton",
        "New Mexico" : "Santa Fe",
        "New York" : "Albany",
        "North Carolina" : "Raleigh",
        "North Dakota" : "Bismarck",
        "Ohio" : "Columbus",
        "Oklahoma" : "Oklahoma City",
        "Oregon" : "Salem",
        "Pennsylvania" : "Harrisburg",
        "Rhode Island" : "Providence",
        "South Carolina" : "Columbia",
        "South Dakota" : "Pierre",
        "Tennessee" : "Nashville",
        "Texas" : "Austin",
        "Utah" : "Salt Lake City",
        "Vermont" : "Montpelier",
        "Virginia" : "Richmond",
        "Washington" : "Olympia",
        "West Virginia" : "Charleston",
        "Wisconsin" : "Madison",
        "Wyoming" : "Cheyenne"}

    correct = 0
    incorrect = 0
    keep_going = 'y'
    while keep_going.lower() == 'y':
        random_state = random.choice(list(state_capitals.keys()))
        answer = input(f"What is the capital of {random_state}? ").strip()
        if answer.lower() == state_capitals[random_state].lower():
            print("Correct!")
            keep_going = str(input("Would you like to continue (y/n)? "))
            correct += 1

        else:
            print(f"This answer is incorrect.")
            keep_going = str(input("Would you like to continue (y/n)? "))
            incorrect += 1

    print(f'''YOUR SCORE: 
Correct: {correct} 
Incorrect: {incorrect}''')

if __name__ == "__main__":
    main()