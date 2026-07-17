from google import genai
import os

api=os.getenv("GOOGLE_API_KEY_ASSIST_BOT_02")
client=genai.Client(api_key=api)

print(f"API KEY : {api}")

working_model=None

for model in client.models.list():
    model_name=model.name.replace("models/","")
    try:
        client.models.generate_content(
        model=model_name,
        contents="Hello")
        working_model=model_name
        print(f"Working Modl : {model_name}")
        break
    except Exception:
            continue
    
if working_model is None:
     print("There is no Working model available now")
     exit()


history=[]

print("AI ASSIST BOT")
print("(type 'exit' to quit) \n")

while True:
    user=input("user : ")
    if user.lower()=="exit":
        break
    history.append(f"User: {user}")
    prompt="\n".join(history)

    response=client.models.generate_content(
        model=working_model,
        contents=prompt
    )

    answer=response.text

    print(f"AI Bot: {answer}")

    history.append(f"Assistant: {answer}")
