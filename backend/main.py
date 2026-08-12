from fastapi import FastAPI


app = FastAPI(
    title="AI Cooking Assistant"
)


@app.get("/")
def home():
    return {
        "message": "AI Cooking Assistant is running"
    }