from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import traceback
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows the frontend to access the backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI()

class TextInput(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API is running"}

def analyze_sentiment(text):
    try:
        logger.debug(f"Analyzing sentiment for text: {text}")
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a sentiment analysis expert. Provide a verbose analysis of the sentiment in the given text."},
                {"role": "user", "content": f"Analyze the sentiment of this text: {text}"}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        error_details = traceback.format_exc()
        logger.error(f"Error in analyze_sentiment: {str(e)}\n{error_details}")
        raise HTTPException(status_code=500, detail=f"Error analyzing sentiment: {str(e)}\n\nDetails:\n{error_details}")

@app.post("/analyze_sentiment")
async def sentiment_analysis(input: TextInput):
    try:
        sentiment_analysis = analyze_sentiment(input.text)
        return {"sentiment_analysis": sentiment_analysis}
    except HTTPException as e:
        logger.error(f"HTTPException in sentiment_analysis: {e.detail}")
        raise e
    except Exception as e:
        error_details = traceback.format_exc()
        logger.error(f"Unexpected error in sentiment_analysis: {str(e)}\n{error_details}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}\n\nDetails:\n{error_details}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)