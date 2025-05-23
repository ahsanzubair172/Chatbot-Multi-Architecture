from llama_index.llms.groq import Groq
from API import MyApi

# Initialize Groq
llm = Groq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct", 
    api_key=MyApi,  
    max_tokens=1000,
    temperature=0.7,
    top_p=0.9,
    num_beams=4,
    do_sample=True
)


print("Welcome to Groq Chat! (Type 'quit' | 'close' to exit)")
print("-" * 50)
    
while True:
    
    user_input = input("\nYou: ").strip()
        
    if user_input.lower() in ['quit', 'close']:
        print("\nGoodbye!")
        break
    try:
        response = llm.complete(user_input)
        print("\nBot:", response.raw)
    except Exception as e:
        print(f"An error occurred: {e}")
        

