from google import genai
from google.genai import types
import os

PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

def assess_risk():
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

    scenario = """
    Scenario: "The applicant, 'The Fiery Grill,' is a new upscale restaurant specializing in wood-fired oven pizzas. 
    They have installed a new fire suppression system but it is not yet certified. 
    They plan to feature live acoustic music and offer valet parking."
    """

    prompt = "Based on this scenario, list three primary risk factors an underwriter should consider."
    
    system_instruction = "You are an insurance risk analyst assistant. Identify potential risk factors concisely."

    print("Analyzing risk scenario...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(role="user", parts=[types.Part.from_text(text=scenario + prompt)])
        ],
        config=types.GenerateContentConfig(
            temperature=0.2,
            system_instruction=[types.Part.from_text(text=system_instruction)],
        )
    )

    print(response.text)

if __name__ == "__main__":
    assess_risk()
