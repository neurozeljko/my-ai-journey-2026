import vertexai
from vertexai.generative_models import GenerativeModel, Part
import json

def generate_furniture_recommendations(room_image_uri):
    """
    Koristi Gemini kao 'Interior Design Expert-a'.
    Analizira sobu i vraca strukturirani JSON sa preporukama.
    """
    model = GenerativeModel("gemini-1.0-pro-vision")
    
    # Prompt inženjering za strukturirani izlaz (Senior skill)
    prompt = """
    You are an expert interior designer. Analyze the uploaded image of a living room.
    Identify the design style (e.g., Modern, Scandinavian, Industrial).
    Based on the style, recommend 3 furniture items to add.
    
    Return the response strictly as a JSON object with this schema:
    {
        "design_style": "string",
        "recommendations": [
            {"item": "string", "reason": "string", "suggested_color": "string"}
        ]
    }
    """
    
    image = Part.from_uri(uri=room_image_uri, mime_type="image/jpeg")
    
    response = model.generate_content(
        [image, prompt],
        generation_config={"temperature": 0.2, "response_mime_type": "application/json"}
    )
    
    return response.text

if __name__ == "__main__":
    print("--- Generisanje Retail Preporuka ---")
    # Simulacija poziva
    # print(generate_furniture_recommendations("gs://your-bucket/room.jpg"))
