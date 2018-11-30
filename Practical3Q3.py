''' A which takes in a students score and gives back their grades 
The following table illustrates the cutoff scores for the various academic grades in a school. Write a program that will prompt the student for his score and your program should display his grade. 

Grade
80 and above
‘A’
70 to 79
‘B’
60 to 69
‘C’
50 to 59
‘D’
49 and below
‘F’
'''


print("Enter Your Score")
score = int(input())

if score < 49:
    print("F")

elif score >= 50 and score <= 59:
    print("D")

elif score >= 60 and score <= 69:
    print("C")

elif score >= 70 and score <= 79:
    print("B")

elif score >= 80:
    print("A")
