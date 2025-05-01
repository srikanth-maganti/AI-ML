import ollama
response=ollama.list()
# print(response)


res=ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"why is sky is blue?"
        },
    ],
)

# print(res["message"]["content"])

res=ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"what can u do?"
        },
    ],
    stream=True,

)

# for chunk in res:
#     print(chunk["message"]["content"],end="",flush=True)

# ==== The Ollama Python library's API is designed around the Ollama REST API ====
res=ollama.generate(
    model="llama3.2",
    prompt="why is sky is blue?",
)

# print(res["response"])

print(ollama.show("llama3.2"))






# ollama.delete("knowitall")