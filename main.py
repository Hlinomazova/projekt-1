"""
main.py: první projekt do Engeto Online Python Akademie

author: Kristýna Hlinomazová
email: k.hlinomazova@gmail.com
"""

# Zadání přihlašovacích údajů
username = input("Enter your username: ")
password = input("Enter your password: ")

# Registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Ověření přihlášení
if username in users and users[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
else:
    print("----------------------------------------")
    print("Unregistered user, terminating the program.")
    print("----------------------------------------")
    exit()

# Výběr textu
choice = int(input("Enter a number between 1 and 3 to select: "))

if choice == 1:
    selected_text = TEXTS[0]
elif choice == 2:
    selected_text = TEXTS[1]
elif choice == 3:
    selected_text = TEXTS[2]
else:
    print("----------------------------------------")
    print("Invalid choice. Terminating the program.")
    print("----------------------------------------")
    exit()

# Rozdělení textu na slova dle mezer 
words = selected_text.split()

# Počet slov v textu 
word_count = len(words)

print(f"There are {word_count} words in the selected text.")

# Počet slov začínajících velkým písmenem
titlecase_count = 0

for word in words:
    if word.istitle():
        titlecase_count += 1

print(f"There are {titlecase_count} titlecase words.")

# Počet slov psaných velkými písmeny 

uppercase_count = 0

for word in words:
    if word.isupper():
        uppercase_count += 1

print(f"There are {uppercase_count} uppercase words.")       

# Počet slov psaných malými písmeny

lowercase_count = 0

for word in words:
    if word.islower():
        lowercase_count += 1

print(f"There are {lowercase_count} lowercase words.")   

# Počet a suma čísel 

number_count = 0
number_sum = 0

for word in words:
    if word.isdigit():
        number_count +=1
        number_sum = number_sum + int(word)

print(f"There are {number_count} numeric strings.")
print(f"The sum of all numbers is {number_sum}.")

# Sloupcový graf 

lengths = {}

for word in words:
    word = word.strip(".,!?")
    length = len(word)
    if length in lengths:
        lengths[length] += 1
    else:
        lengths[length] = 1

print("----------------------------------------")
print("LEN| OCCURRENCES |NR.")
print("----------------------------------------")

for length in sorted(lengths):
    count = lengths[length]
    stars = "*" * count
    print(f"{length:>3}|{stars:<13}|{count}")