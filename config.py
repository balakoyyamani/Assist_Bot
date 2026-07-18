from google import genai
import os

api=os.getenv("GOOGLE_API_KEY_ASSIST_BOT_02")
if not api:
    print("API KEY is not loaded 😢")
    exit()
print("API KEY is loaded 🥳")

client=genai.Client(api_key=api)

def get_working_model():

    for model in client.models.list():
        model_name=model.name.replace("model/","")
        
        try:
            client.models.generate_content(
                model=model_name,
                contents="Hello"
            )
            working_model=model_name
            print(f"Working Model : {working_model}")
            return model_name
        except Exception as e:
            continue
        
    print("There is no Model available now😢")
    exit()




