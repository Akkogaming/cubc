from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS so your Vite frontend (port 5173) can communicate with Python (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the structure of data you expect from Vite
class DataInput(BaseModel):
    text: str

# Your custom Python function
def process_data(input_string: str) -> str:
    return f"Python processed: {input_string.upper()}!"

# Expose the function via a POST route
@app.post("/api/process")
async def run_function(payload: DataInput):
    result = process_data(payload.text)
    return {"status": "success", "output": result}

if __name__ == "__test__":
    import uvicorn
    uvicorn.run("test:app", host="127.0.0.1", port=8000, reload=True)
