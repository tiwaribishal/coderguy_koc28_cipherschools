# the task is to generate a random story every time user run the program

import random

when = ["A few years ago", "Yesterday", "Last night","Along time ago", "on 26 November"]

who = [" a Lion","a Tiger","a Cow", "a Mouse"," a Dog"]

name = ["bishal", "Abhisekh", "Awnit", "priyansh","aditya","prasaant"]

residence = ["Mumbai", "New delhi" , "chennai", "kolkata","patna","Lucknow","punjab"]

went = ["college","cienema", "school","university","Mall"]

happened = ["made a lot  of freinds","Eats a burger", "found a secret key","solved a problem", "wrote a book", "play with freind"]

print(random.choice(when)+', '+ random.choice(name)+' that lived in '+random.choice(residence)+', went to the '+random.choice(went)+' and '+random.choice(happened))