import os 
from openai import OpenAI
key = "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"


message = []
client = OpenAI(api_key=key)
 
def completion(message):
    global messages
    chat_completion = client.chat.completions.create(
        messages.append({"role": "user", "content": message}),
        
        model="gpt-3.5-turbo",
    )

    print(chat_completion)
if __name__ == "__main__":
    user_question = input("hi i am jarvis,how i can help you?")
    completion(user_question)