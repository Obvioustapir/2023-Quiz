import random

#main routine goes here.

question = ["what is the sybol for lithium on the periodic table?", "how many bones are in the human body?", "what is the name of the native New zealand green parrot?", "What city in New Zealand has the tallest building?"]

#testing loop to generate 10 questions.
for item in range (0,1):
  chosen = random.choice(question)
  print(chosen)




