#functions go here...
def difficulty(question):
  valid = False
  while not valid:
#Ask the user if they have played before
    response = input(question).lower()
#if they input yes, line of code replys 'program continues'.
    if response == "easy" or response == "e":
      response = "easy"
      return response
#if the user inputs no the program will display instructions for the game.
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
  ask_difficulty = difficulty ("Would you like to answer an easy, medium or hard question.")
  #provide feedback
  if ask_difficulty == "medium":
    print("you will be playing for $2")
  elif ask_difficulty == "easy":
    print("you will be playing for $1")
  elif ask_difficulty == "hard":
    print("you will be playing for $3")