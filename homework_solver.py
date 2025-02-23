import ollama

# Specify the desired model (ensure it matches one listed by 'ollama list')
model_name = "llama3.2:3b"

print("Type exit() to exit the program.")

def give_hint(prompt):
    if prompt == "exit()":
        return

    # Send the chat request to the model
    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Extract and print the response content
    print("Llama AI: ", response["message"]["content"])

# Define the query or prompt
while True:
    num_of_hints = int(input("How many hints would you like? "))
    question = input("Question: ")
    give_hint(f"Please give a hint for this question: " + question)

    for i in range(num_of_hints-1):
        another_hint = input("Do you want another hint? yes/no ").lower()
        if another_hint != "yes" and another_hint != "no":
            print("Invalid input.")
            break
        elif another_hint == "yes":
            give_hint(f"Please give a hint for this question: " + question)
        else:
            break

    user_continue = input("Do you want to ask another question? yes/no ").lower()

    if user_continue != "yes" and user_continue != "no":
        print("Invalid input.")
    elif user_continue == "no":
        break