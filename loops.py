# range(5)
# 0,1,2,3,4

for number in range(5):
    print("The number is", number)

# starts at 1 stops at 5 , the last parameter is exclusive
for number in range(1, 6):
    print("The number is", number)

# steps
for number in range(1, 10, 2):
    print("The number is", number)

# decrement, 1 is exclusive here
for number in range(6, 1, -1):
    print("The number is", number)

#for loops with strings
sentence = "The quick brown fox"
for character in sentence:
    print(character)

#In class question to solve
for x in range(100):
    print("We like to code")