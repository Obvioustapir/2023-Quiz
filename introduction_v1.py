#functions go here...
def introduction(question):
  valid = False
  while not valid:
#Ask the user if they have played before
    response = input(question).lower()
#if they input yes, line of code replys 'program continues'.
    if response == "yes" or response == "y":
      response = "yes"
      return response
#if the user inputs no the program will display instructions for the game.
    elif response == "no" or response == "n":
      response = "no"
      return response
    else:
      print("please answer yes / no")

#loop for testing
show_instructions = ""
while show_instructions != "xxx":
  show_instructions = introduction ("have you played the game before? ")
  #provide feedback
  if show_instructions == "yes":
    print("programm continues")
  elif show_instructions == "no":
    print("display instructions")