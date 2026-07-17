from google import genai
import os

api=os.getenv("GOOGLE_API_KEY_ASSIST_BOT_02")
client=genai.Client(api_key=api)

print(api)

history=[]

print("AI ASSIST BOT")
print("type 'exit' to quit \n")

while True:
    user=input("user : ")
    if user.lower()=="exit":
        break
    history.append(f"User: {user}")
    prompt="".join(history)

    response=client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    answer=response.text

    print(f"AI Bot: {answer}")

    history.append(f"Assistant: {answer}")