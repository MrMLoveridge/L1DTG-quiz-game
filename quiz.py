def ask(question, answer):
  print(question)
  user_response=input().lower()
  if user_response == answer:
    print("Correct")
  else:
    ask(question,answer)
    
    
ask("what is blue?","a color")
