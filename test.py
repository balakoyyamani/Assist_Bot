from config import get_working_model
from chat import chat
from history import load_history,save_history,clear_history
history=[]
#chat(get_working_model(),history,"hello,I am Bala")

print(load_history())
save_history(["Ram","Sita"])
clear_history()