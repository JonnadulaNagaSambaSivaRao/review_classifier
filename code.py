from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("=" * 50)
print("Customer Review Classifier")
print("Type 'exit' to quit")
print("=" * 50)

# Context Engineering (stores conversation history)
messages = [
    {
        "role": "system",
        "content": """
You are a sentiment analysis expert.

Your job is to classify every customer review into one of these categories:
1. Positive
2. Neutral
3. Negative

Rules:
- Return only one category name.
- Do not provide explanations.
- Consider the overall emotion and meaning of the review.
- Remember previous conversation context.
- If the user asks about previous reviews, answer based on the conversation history.
"""
    }
]

# Continuous chat loop
while True:

    review = input("\nEnter customer review: ")

    if review.lower() == "exit":
        print("\nSession Ended.")
        break

    # Add user input
    messages.append(
        {
            "role": "user",
            "content": review
        }
    )

    # Call Groq API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0
    )

    result = response.choices[0].message.content

    print("\nReview Classification:")
    print(result)

    # Save assistant response
    messages.append(
        {
            "role": "assistant",
            "content": result
        }
    )
