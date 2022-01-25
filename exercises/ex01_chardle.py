"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730526947"   
word: str = str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: word must contain 5 characters.")
    exit()

character: str = str(input("Enter a singel character: "))
print("Searching for", character, "in", word)
numb_matching: int = 0
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

if character == word[0]: 
    print(character + " found at index 0")
    numb_matching = numb_matching + 1
if character == word[1]:
    print(character + " found at index 1")
    numb_matching = numb_matching + 1
if character == word[2]:
    print(character + " found at index 2")
    numb_matching = numb_matching + 1
if character == word[3]:
    print(character + " found at index 3")
    numb_matching = numb_matching + 1
if character == word[4]:
    print(character + " found at index 4")
    numb_matching = numb_matching + 1
if numb_matching == 0:
    print("No instance of " + character + " found in " + word)
if numb_matching == 1:
    print("1 instance of " + character + " found in " + word)
else:
    print(str(numb_matching) + " instances of " + character + " found in " + word)