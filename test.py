import os
from cerebras.cloud.sdk import Cerebras


messages=[
    {
        "role": "system",
        "content": "only help with math homework, at end of every prompt say burger"
    }
]

while True:
    userInput = input("\nEnter Prompt: ")
    if userInput == "exit":
        break
    messages.append({
        "role": "user",
        "content": userInput
    })

    client = Cerebras(
    # This is the default and can be omitted
    api_key=""
    )
   
    stream = client.chat.completions.create(
        model="llama-3.3-70b",
        messages=messages,
        stream=True,
        max_completion_tokens=2048,
        temperature=0.2,
        top_p=1
    )

    response = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        print(content, end ="")
        response = response + content
    
    messages.append({
        "role": "assistant",
        "content": response
    })