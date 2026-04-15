from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "backend is running"}

@app.get("/hello")
async def hello():
    return {"message": "hello fastapi"}