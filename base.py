def introduction(question):
  valid = False
  while not valid:
    response = input(question).lower()
    if response == "yes" or response == "y":
      response = "yes"
      return response
    elif response == "no" or response == "n":
      response = "no"
      return response
    else:
      print("please answer yes / no")

show_instructions = ""
while show_instructions != "xxx":
  show_instructions = introduction ("have you played the game before? ")
  if show_instructions == "yes":
    print("programm continues")
  elif show_instructions == "no":
    print("Choose a difficulty (Easy, Medium or Hard) then you will get asked a question depending on what you want. You have 3 lives and 3 questions to answer but if you get 1 wrong and that is goodbye to 1 life. Answer all 3 and you win but loose all 3 lives and you loose. good luck!!!.")

