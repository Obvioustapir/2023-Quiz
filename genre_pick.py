#functions go here...
def genres (question):
  valid = False
  while not valid:
#Ask the user if they have played before
    response = input(question).lower()
#if they input yes, line of code replys 'program continues'.
    if response == "science" or response == "sci":
      response = "science"
      return response
#if the user inputs no the program will display instructions for the game.
    elif response == "sports" or response == "spo":
      response = "sports"
      return response
    elif response == "history" or response == "his":
      response = "history"
      return response
    elif response == "math" or response == "mat":
      response = "math"
      return response
    elif response == "nature" or response == "nat":
      response = "nature"
      return response
    elif response == "animals" or response == "ani":
      response = "animals"
      return response
    elif response == "spelling" or response == "spe":
      response = "spelling"
      return response
    else:
      print("Please enter one of the prefered genre's")

#loop for testing
pick_genre = ""
while pick_genre != "xxx":
  pick_genre = genres ("Please pick a genre the genre's are - science, sports, history, math, nature, animals and spelling .")
  #provide feedback
  if pick_genre == "science":
    print("You have picked science ")
  elif pick_genre == "sports":
    print("You have picked sports")
  elif pick_genre == "history":
    print("You have picked history")
  elif pick_genre == "math":
    print("You have picked math")
  elif pick_genre == "nature":
    print("You have picked nature")
  elif pick_genre == "animals":
    print("You have picked animals")
  elif pick_genre == "spelling":
    print("You have picked spelling")