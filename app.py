from google import genai
import os

api=os.getenv("GOOGLE_API_KEY_ASSIST_BOT_02")
if api:
     print("API KEY LOADED🥳")
else:
     print("API KEY IS NOT LOADED😢")
     exit()

client=genai.Client(api_key=api)

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
system_prompt = """
You are a helpful AI tutor.

Explain everything simply.

Always use examples.

Keep answers concise.
"""

while True:
    user=input("user : ").strip()
    if not user:
         print("Enter the Message :")
         continue
    if user.lower()=="exit":
        break
    history.append(f"User: {user}")
    prompt=system_prompt+"\n\n"+"\n".join(history)
    full_response=""
    print("AI Bot : ",end="",flush=True)
    try:
        stream=client.models.generate_content_stream(
            model=working_model,
            contents=prompt
            )

        for chunk in stream:
            if chunk.text:
                print(chunk.text,end="",flush=True)
                full_response+=chunk.text
        print("\n")              

        history.append(f"Assistant: {full_response}")
    except Exception as e:
         print(f"Error : {e}")
         continue

print("Thanks for Chatting! 😊")