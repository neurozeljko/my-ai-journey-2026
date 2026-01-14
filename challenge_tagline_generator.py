# Vertex AI - Tagline Generator Challenge
# Description: Generates marketing taglines based on brand persona and specific keywords.
# Technologies: Google Gen AI SDK, System Instructions, Few-Shot Prompting

from google import genai
from google.genai import types

# Placeholder Configuration
PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

def generate_marketing_tagline():
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
    model = "gemini-2.5-flash"

    # 1. System Instructions (Brand Context)
    text_si = """Cymbal Direct is partnering with an outdoor gear retailer. 
    They're launching a new line of products designed to encourage young people to explore the outdoors. 
    Help them create catchy taglines for this product line."""

    # 2. Few-Shot Examples (Learning from history)
    history_examples = [
        types.Content(role="user", parts=[types.Part.from_text(text="Write a tagline for a durable backpack designed for hikers that makes them feel prepared. Consider styles like minimalist.")]),
        types.Content(role="model", parts=[types.Part.from_text(text="Built for the Journey: Your Adventure Essentials.")]),
    ]

    # Create Chat Session
    chat = client.chats.create(
        model=model,
        config=types.GenerateContentConfig(
            temperature=1, 
            system_instruction=[types.Part.from_text(text=text_si)],
        ),
        history=history_examples
    )

    print("Sending prompt with keyword constraint: 'nature'...")

    # 3. Prompt with specific keyword requirement
    response = chat.send_message("Write a catchy tagline for a new outdoor product line. Make sure to include the keyword nature.")

    print(f"Generated Tagline:\n{response.text}")

if __name__ == "__main__":
    generate_marketing_tagline()
