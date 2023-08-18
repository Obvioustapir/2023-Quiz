#functions go here...
def genres (question):
  valid = False
  while not valid:
#Ask the user if they have played before
    response = input(question).lower()
#if they input yes, line of code replys 'program continues'.
#if the user inputs no the program will display instructions for the game.


#loop for testing
pick_genre = ""
while pick_genre != "xxx":
  pick_genre = genres ("Please pick a genre the genre's are - science, sports, history, math, nature, animals and spelling .")
  #provide feedback

