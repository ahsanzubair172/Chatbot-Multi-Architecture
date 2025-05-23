from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_index.llms.groq import Groq 
from API import MyApi

# FastAPI app
app = FastAPI()

# Init LLM
llm = Groq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    api_key=MyApi,
    max_tokens=512,
    temperature=0.6,
    top_p=0.9,
    top_k=50,
    num_beams=4,
    do_sample=True
)



# Input model
class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    user_input = msg.message.strip()
    if user_input.lower() in ["exit", "quit", "bye"]:
        return {"response": "Goodbye!"}
    
    try:
        result = llm.complete(user_input)
        return {"response": result.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
