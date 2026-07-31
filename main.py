from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Get customer review
review = input("Enter customer review:\n")

# Prompt Engineering
prompt = f"""
You are a sentiment analysis expert.

Classify the customer review into one of these categories:
1. Positive
2. Neutral
3. Negative

Rules:
- Return only one category name.
- Do not provide explanations.
- Consider the overall emotion and meaning of the review.

Customer Review:
{review}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

result = response.choices[0].message.content

print("\nReview Classification:")
print(result)