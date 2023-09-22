# Read the character
char = input()

# Read the list of words
words = input().split()

# Initialize an empty list to store words containing the character
result = []

# Iterate through each word and check if it contains the character
for word in words:
    if char in word:
        result.append(word)

# Output the words containing the character
for word in result:
    print(word)
