import json
import os

History_File="history.json"
def load_history():
    if not os.path.exists(History_File):
        with open(History_File,"w") as file:
            json.dump([],file)
    
    with open(History_File,"r") as file:
        return json.load(file)

def save_history(history):
    with open(History_File,"w") as file:
        json.dump(history,file,indent=4)

def clear_history():
    save_history([])