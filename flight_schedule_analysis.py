from google import genai
from google.genai import types
import os

PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

def analyze_flight_schedule():
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

    # Slika reda letenja (Zameniti pravom putanjom u produkciji)
    image_file = types.Part.from_uri(
        file_uri="gs://cloud-samples-data/generative-ai/image/timetable.png",
        mime_type="image/png",
    )

    prompt_text = """
    1. Provide a concise title for this image.
    2. Extract all visible text. Present the flight schedule as a clearly formatted list.
    3. Calculate: What percentage of flights depart before 11:30 AM?
    """

    print("Analyzing flight schedule image...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(role="user", parts=[image_file, types.Part.from_text(text=prompt_text)])
        ],
        config=types.GenerateContentConfig(
            temperature=0.2,
            top_p=1,
            max_output_tokens=2048
        )
    )
    
    print(response.text)

if __name__ == "__main__":
    analyze_flight_schedule()
