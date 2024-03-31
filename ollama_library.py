
import ollama

stream = ollama.chat(
    model="bot1",
    messages=[{"role":"user",
               'content':'who sre you ?'}],
               stream=True
    )



for chunk in stream:
    console.print(chunk['message']['content'], end='')