from llama_index import LLMPredictor, ServiceContext
from llama_index.llms.groq import Groq
from API import MyApi

# Initialize LLM with history support
llm = Groq(model="meta-llama/llama-4-maverick-17b-128e-instruct", api_key=MyApi)
predictor = LLMPredictor(llm=llm)
service_context = ServiceContext.from_defaults(llm_predictor=predictor)

chat_history = []

print("Chatbot is ready! Type 'exit' to end.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    
    # Create prompt with history
    prompt = f"Conversation history:\n{chat_history}\nUser: {user_input}\nAssistant:"
    
    # Get response
    response = llm.complete(prompt)
    
    # Update chat history
    chat_history.append(f"User: {user_input}\nAssistant: {response}")
    
    print(f"Chatbot: {response}")