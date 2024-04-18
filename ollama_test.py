import requests

url = 'http://localhost:11434/api/generate'

while True:
    prompt = input("Prompt: ")

    data = {
        "model" : "gemma",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    print(f"\nAI:\n\n {response.json()['response']}\n")