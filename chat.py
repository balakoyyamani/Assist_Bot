from config import client

system_prompt="""You are a helpful AI tutor.
                Explain everything simply."""

def chat(model,history,user_msg):
    history=history[-20:]
    history.append(f"User : {user_msg}")
    prompt=system_prompt+"\n\n"+"\n".join(history)
    
    stream=client.models.generate_content_stream(
        model=model,
        contents=prompt
    )
    print("AI Tutor : ",end="",flush=True)
    full_response=""
    for chunk in stream:
        if chunk.text:
            print(chunk.text,end="",flush=True)
            full_response+=chunk.text
    print("\n")
    history.append(f"AI Tutor : {full_response}")
    return history



