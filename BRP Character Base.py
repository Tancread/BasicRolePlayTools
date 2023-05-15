import random

# Define the character creation rules
attributes = ['STR', 'CON', 'DEX', 'SIZ', 'INT', 'POW', 'CHA']
skills = ['Art', 'Athletics', 'Bargain', 'Brawl', 'Craft', 'Dodge', 'Drive', 'Firearms', 'First Aid', 'History', 'Language', 'Law', 'Medicine', 'Melee', 'Occult', 'Persuade', 'Pilot', 'Psychoanalysis', 'Psychology', 'Ride', 'Science', 'Sleight of Hand', 'Spot Hidden', 'Stealth', 'Survival']

# Ask the user for input
name = input("Enter character name: ")
gender = input("Enter character gender: ")
occupation = input("Enter character occupation: ")

# Generate attribute and skill values
attribute_values = {}
skill_values = {}
for attribute in attributes:
    value = random.randint(1, 6) + random.randint(1, 6) + 6
    attribute_values[attribute] = value * 5
for skill in skills:
    skill_values[skill] = random.randint(0, 100)

# Display character information
print(f"\nName: {name}\nGender: {gender}\nOccupation: {occupation}\n")
print("Attributes:")
for attribute in attributes:
    print(f"{attribute}: {attribute_values[attribute]}")
print("\nSkills:")
for skill in skills:
    print(f"{skill}: {skill_values[skill]}")

# Save character information to a file
save_to_file = input("Do you want to save this character to a file? (y/n) ")
if save_to_file.lower() == 'y':
    with open(f"{name}.txt", "w") as file:
        file.write(f"Name: {name}\nGender: {gender}\nOccupation: {occupation}\n")
        file.write("\nAttributes:\n")
        for attribute in attributes:
            file.write(f"{attribute}: {attribute_values[attribute]}\n")
        file.write("\nSkills:\n")
        for skill in skills:
            file.write(f"{skill}: {skill_values[skill]}\n")