"Quick brown fox jumps over the lazy dog"

def b1(given_sentence):
    given_sentence = given_sentence.replace('.', '') 
    a1 = given_sentence.split()
    return a1
given_sentence = "Quick brown fox jumps over the lazy dog."
a1 = b1(given_sentence)
print("Tokenized Sentence without full stop: ", a1)

#type: ignore

users = [
    {"id" :0, "name":"Hero"},
    {"id" :1, "name":"Dunn"},
    {"id" :2, "name":"Sue"},
    {"id" :3, "name":"Chi"},
    {"id" :4, "name":"Thor"},
    {"id" :5, "name":"Clive"},
    {"id" :6, "name":"Hicks"},
    {"id" :7, "name":"Devin"},
    {"id" :8, "name":"Kate"},
    {"id" :9, "name":"Klein"},
]

friendships_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                     (4,5), (5,6), (5,7), (6,8), (7,8), (8,9) ] 
# to create a dictionary where the  


my_dict = {}
print(my_dict)
pairs = {user["id"]: [] for user in users}

for i, j in friendships_pairs:
    pairs[i].append(j)
    pairs[j].append(i)

#printing the result
print(pairs) 


#Taking a 4 digit number from the user convert the number into hrs, intues and second and show the result it into seconds 

# Input a 4-digit number from the user
number = int(input("Enter a 4-digit number: "))

# Extract hours, minutes, and seconds from the number
hours = number // 10000
minutes = (number % 10000) // 100
seconds = number % 100

# Convert everything into total seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# Output the result
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
print(f"Total time in seconds: {total_seconds}")


#11 September 2024
str.maketrans
str.punctuation

import string

def tokenise_and_remove_punctuation(text):
    text = text.translate(str.maketrans("","", string.punctuation))#One is instance method and the other one is the class method
    #.translate could translate something
    tokens = text.split()
    return tokens

# write a code to enter an input string from the user in a long sentence and then repalce the words with the other words and also delete 
# some words in a sentence.



