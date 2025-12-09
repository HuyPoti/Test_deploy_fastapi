from fastapi import FastAPI
import uvicorn
import os


app = FastAPI()

# Example route: Home
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Example route: Item with ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Example route: About
@app.get("/about")
def about():
    return {"info": "This is an example FastAPI application."}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="127.0.0.1", port=port)