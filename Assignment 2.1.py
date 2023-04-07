# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 2

# Problem 1 - Encryption

# Get an input from the user
text_input = input("Input a plaintext: ")
text_output = ""

# Check if the input has the variables and change it into corresponding symbols
for i in range(len(text_input)):
# If there is 'a', change to '*'
    if text_input[i].lower() == 'a':
        text_output += '*'
# If there is 'e', change to '&'
    elif text_input[i].lower() == 'e':
        text_output += '&'
# If there is 'i', change to '#'
    elif text_input[i].lower() == 'i':
        text_output += '#'
# If there is 'o', change to '+'
    elif text_input[i].lower() == 'o':
        text_output += '+'
# If there is 'u', change to '!'
    elif text_input[i].lower() == 'u':
        text_output += '!'
    else:
        text_output += text_input[i]
# Print the encrypted input
print(text_output)