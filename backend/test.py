#!/usr/bin/env -S poetry run python
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

def analyze_sentiment(text, stream=False):
    messages = [
        {"role": "system", "content": "You are a sentiment analysis expert. Provide a verbose analysis of the sentiment in the given text."},
        {"role": "user", "content": f"Analyze the sentiment of this text: {text}"}
    ]
    
    if stream:
        return client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            stream=True
        )
    else:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        return completion.choices[0].message.content

if __name__ == "__main__":
    # Standard request
    print("----- Standard Sentiment Analysis -----")
    test_text = "I love this product! It's amazing and works perfectly."
    result = analyze_sentiment(test_text)
    print(result)

    # Streaming request
    print("\n----- Streaming Sentiment Analysis -----")
    stream = analyze_sentiment("This movie was terrible. I hated every minute of it.", stream=True)
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    print()

    # Custom response headers
    print("\n----- Custom Response Headers Test -----")
    response = client.chat.completions.with_raw_response.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis expert. Provide a brief analysis of the sentiment in the given text."},
            {"role": "user", "content": "Analyze the sentiment of this text: The weather today is just perfect!"}
        ]
    )
    completion = response.parse()
    print(f"Request ID: {response.headers.get('x-request-id')}")
    print(f"Sentiment Analysis: {completion.choices[0].message.content}")

    # Interactive mode
    print("\n----- Interactive Sentiment Analysis -----")
    while True:
        user_input = input("\nEnter text to analyze (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        result = analyze_sentiment(user_input)
        print("Sentiment Analysis Result:")
        print(result)