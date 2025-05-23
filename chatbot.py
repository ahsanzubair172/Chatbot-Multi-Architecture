import os
from API import MyApi
from typing import List
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.core.indices.vector_store.base import VectorStoreIndex
from llama_index.core import ServiceContext
# from llama_index import VectorStoreIndex, ServiceContext 
from llama_index.llms.groq import Groq # type: ignore
from llama_index.embeddings import GroqEmbedding  

# Setting  Groq API key in the environment variable
os.environ["GROQ_API_KEY"] = "MyApi"  

def load_context_data(file_paths: List[str]) -> List:
    """Load and process context data from files."""
    # Use SimpleDirectoryReader to load data from the provided file paths
    documents = SimpleDirectoryReader(input_files=file_paths).load_data()
    return documents

def setup_index(context_data: List) -> VectorStoreIndex:
    """Set up LlamaIndex with Groq embeddings."""
    # Initialize Groq embeddings using GroqEmbedding directly
    groq_embedding = GroqEmbedding()
    
    # Configure the service context with Groq LLM and embeddings
    service_context = ServiceContext.from_defaults(
        llm=Groq(model_name="meta-llama/llama-4-maverick-17b-128e-instruct"),  #  Groq LLM
        embed_model=groq_embedding  # Use Groq embeddings
    )
    
    # Create a vector store index from the context data
    index = VectorStoreIndex.from_documents(
        context_data,
        service_context=service_context
    )
    return index

def chatbot(query_engine, prompt):
    """Query the chatbot and return the response."""
    # Use the query engine to generate a response based on the prompt
    response = query_engine.query(prompt)
    return response

def main():
    """Main function to run the chatbot."""
    # Specify the path to your context files
    context_files = [r"C:\Users\HP\Downloads\Tasks Report.txt"]  #  context file
    
    # Load the context data from the files
    context_data = load_context_data(context_files)
    
    # Set up the index with the loaded context data
    index = setup_index(context_data)
    
    # Creating a query engine from the index
    query_engine = index.as_query_engine()

    print("Chatbot is running! Type 'exit' or 'quit' to stop.")
    
    # Start the chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
            
        # Get the chatbot's response
        answer = chatbot(query_engine, user_input)
        print("Bot:", answer)

if __name__ == "__main__":
    main()