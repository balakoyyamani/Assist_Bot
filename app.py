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
    history=chat(model,history,user)
    save_history(history)
    
print("Thanks You 😊")
