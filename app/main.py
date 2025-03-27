from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Argo CD with GitHub Actions using FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
