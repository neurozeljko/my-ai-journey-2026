from google import genai
from google.genai import types
import os

PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

def extract_claim_data():
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

    claim_text = """
    Claim Notification:
    "Hi team, just got a call from Mrs. Eleanor Vance, policy #POL458892. 
    She reported a kitchen fire that occurred on May 12th, 2025, around 3 PM. 
    The main damage seems to be to the oven and surrounding cabinets. 
    She thinks the total damage might be around $7,500. No injuries reported."
    """

    extraction_prompt = """
    Extract the following data points from the text:
    - Policy Number
    - Claimant Name
    - Date of Loss
    - Time of Loss
    - Type of Loss
    - Estimated Loss Amount
    - Injuries Reported
    
    Output format: Key: Value
    """

    system_instruction = "You are an AI assistant specializing in parsing insurance claims. Extract data accurately."

    print("Extracting claim data...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(role="user", parts=[types.Part.from_text(text=claim_text + extraction_prompt)])
        ],
        config=types.GenerateContentConfig(
            temperature=0.1, # Niska temperatura za preciznost
            system_instruction=[types.Part.from_text(text=system_instruction)],
        )
    )

    print(response.text)

if __name__ == "__main__":
    extract_claim_data()
