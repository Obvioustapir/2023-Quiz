#easy questions go here
easy_question = [["what is the sybol for lithium on the periodic table?","li"],["how many bones are in the human body?","206"], ["what is the name of the native New zealand green parrot?", "kakapo"], ["What city in New Zealand has the tallest building?","auckland"]]
#medium questions go here.
medium_question = [["How many valves does the heart have?","4"],["which metal chemical symbol does Fe stand for?","iron"],["what county produces the most coffee in the world?","brazil"],["what is a group of crows called?","murder"]]
#hard questions go here.
hard_question = [["What year was Marmite invented?","1902"],["how many rings does the planet saturn have?","7"],["what is the national animal of germany?","eagle"],["what is the name of the second tallest mountain in the world?","k2"]]
#functions go here...
def difficulty(question):
#Ask the user if they have played before
  response = input(question).lower()
#if they input yes, line of code replys 'program continues'.
  if response == "easy" or response == "e":
    response = "easy"
    return response
  elif response == "medium" or response == "m":
    response = "medium"
    return response
  elif response == "hard" or response == "h":
    response = "hard"
    return response
  else:
    print("Please answer easy, medium or hard.")

#loop for testing
ask_difficulty = ""
while ask_difficulty != "xxx":
  ask_difficulty = difficulty("Would you like to answer an easy, medium or hard question.")
  #provide feedback
  if ask_difficulty == "medium":
    for item in medium_question:
        print(item[0])
        answer = input("Answer: ").lower().strip()
    if answer == item[1]:
          print("Correct")
  elif ask_difficulty == "easy":
    for item in easy_question:
      print(item[0])
      answer = input("Answer: ").lower().strip()
    if answer == item[1]:
      print("Correct")
  else:
    for item in hard_question:
      print(item[0])
      answer = input("Answer: ").lower().strip()
    if answer == item[1]:
     print("Correct")