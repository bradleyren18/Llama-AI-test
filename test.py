import ollama

# Specify the desired model (ensure it matches one listed by 'ollama list')
model_name = "llama3.2:3b"
keep_prompting = True

# Define the query or prompt
while keep_prompting == True:
    prompt = input("Prompt: ")
    if prompt == "exit()":
        break

    # Send the chat request to the model
    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract and print the response content
    answer = response["message"]["content"]
    print("Answer:", answer)
    user_continue = input("Do you want to ask another question? y/n ").lower
    
    if user_continue != "y" and user_continue != "n":
        print("Invalid input.")
    elif user_continue == "n":
        break