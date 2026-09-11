from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "CI/CD Pipeline Project is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
