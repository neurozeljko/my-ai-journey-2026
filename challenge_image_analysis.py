# Vertex AI - Image Analysis Challenge
# Description: Generates a creative description of a product image using Gemini Pro Vision.
# Technologies: Google Gen AI SDK, Python

from google import genai
from google.genai import types

# Placeholder Configuration
PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

def generate_image_description():
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

    # Product image from Cloud Storage
    msg1_image1 = types.Part.from_uri(
        file_uri="gs://qwiklabs-gcp-02-51c9a0779a8c-bucket/cymbal-product-image.png",
        mime_type="image/png",
    )

    # Prompt with constraint: less than 10 words
    prompt_text = "Describe this image in less than 10 words. Be creative, unusual, and unexpected."
    msg1_text1 = types.Part.from_text(text=prompt_text)

    model = "gemini-2.5-flash"
    
    contents = [
        types.Content(
            role="user",
            parts=[msg1_image1, msg1_text1]
        ),
    ]

    # Configuration for maximum creativity (Temperature = 1)
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=1,
        max_output_tokens=2048,
        response_modalities=["TEXT"],
    )

    print("Generating description...")
    
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate_image_description()
