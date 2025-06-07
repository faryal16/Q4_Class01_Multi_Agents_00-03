from fastapi import FastAPI

app = FastAPI()

print("\n\t\t>>> FastAPI app instance created")

@app.get("/")
def read_root():
    print("[/ GET] Handling request at root endpoint")
    return {"message": "Hello from UV (FastAPI + Uvicorn)!"}
