import ollama

# Specify the desired model (ensure it matches one listed by 'ollama list')
model_name = "llama3.2:3b"

print("Type exit() to exit the program.")

# Define the query or prompt
while True:
    prompt = input("Prompt: ")
    if prompt == "exit()":
        break

    # Send the chat request to the model
    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Extract and print the response content
    print("Answer:", response["message"]["content"])
    user_continue = input("Do you want to ask another question? yes/no ").lower()

    if user_continue != "yes" and user_continue != "no":
        print("Invalid input.")
    elif user_continue == "no":
        break