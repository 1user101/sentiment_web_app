from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sentiment import sentiment

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("index.html", "r") as file:
        return HTMLResponse(content=file.read())

# Pydantic model for JSON input validation
class TextInput(BaseModel):
    text: str

@app.post("/analyze-sentiment/")
def analyze_sentiment(text: TextInput):
    result = sentiment(text.text)
    return result  # Return JSON response
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
