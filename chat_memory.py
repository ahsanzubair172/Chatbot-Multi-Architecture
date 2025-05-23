from groq import Groq
from API import MyApi

# Initialize Groq client with the required model and API key
client = Groq(
    model="llama-4-maverick-17b-128e-instruct",  # Specify the model
    api_key=MyApi
)

# Maintain conversation history
chat_history = []  # Create a list to store chat history

print("Chatbot is ready! Type 'exit' to end.")
while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    # Add user message to history
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Get response using Groq's chat API with history
    response = client.chat.completions.create(
        model="llama-4-maverick-17b-128e-instruct",
        messages=chat_history,
        max_tokens=512,
        temperature=0.7
    )

    # Add assistant response to history
    chat_history.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })

    print(f"Chatbot: {response.choices[0].message.content}")
    