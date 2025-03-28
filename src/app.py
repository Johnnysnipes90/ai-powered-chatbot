from fastapi import FastAPI
from src.config.settings import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
def read_root():
    return {"message": f"{settings.app_name} is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)