import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[
        {'role': 'system', 'content': 'You are a helpful AI that can analyze images.'},
        {'role': 'user', 'content': 'What do you see in this image?', 'images': ['panda1.JPG']}
    ]
)

print(response['message']['content'])