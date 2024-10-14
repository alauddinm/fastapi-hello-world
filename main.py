from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World from Route 1!"}


@app.get("/greet")
def read_greet():
    return {"message": "Hello, Greetings from Route 2!"}

