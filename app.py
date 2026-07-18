from config import get_working_model
from chat import chat
from history import load_history,save_history,clear_history

model=get_working_model()
history=load_history()

print("=" * 45)
print("AI ASSIST TUTOR")
print("=" * 45)

while True:
    user=input("User : ").strip()
    if not user:
        print("Enter the Message")
        continue
    if user=="exit":
        break
    if user=="/clear":
        clear_history()
        print("Memory are deleted 😎")
        continue
    if user=="/history":
          print("HISTORY")
          print("=" *45+"\n")
          for data in load_history():
               print(data)
               print("\n"+"_"*100+"\n")
          continue
    if user=="/help":
        print(""" 
              'exit' : to quit the chat. 
              '/clear' : to delete all history. 
              '/history' : to display the history. 
              '/help' : to see available commands""")
        continue
    history=chat(model,history,user)
    save_history(history)
    
print("Thanks You 😊")
