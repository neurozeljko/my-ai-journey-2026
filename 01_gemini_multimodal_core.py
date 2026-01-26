import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Inicijalizacija projekta (Arhitekta uvek definise config na pocetku)
PROJECT_ID = "your-google-cloud-project"
LOCATION = "us-central1"
vertexai.init(project=PROJECT_ID, location=LOCATION)

def analyze_multimodal_content(prompt_text, image_uri):
    """
    Demonstrira multimodalne sposobnosti Gemini Pro Vision modela.
    Analizira sliku i odgovara na prompt.
    """
    # Ucitavanje modela
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

    # Priprema slike (iz GCS-a ili lokalno)
    image = Part.from_uri(
        uri=image_uri,
        mime_type="image/jpeg"
    )

    # Generisanje odgovora
    responses = multimodal_model.generate_content(
        [image, prompt_text],
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 1,
            "top_k": 32
        }
    )
    
    return responses.text

# Primer upotrebe za Portfolio
if __name__ == "__main__":
    print("--- Pokretanje Multimodalne Analize ---")
    # Zameniti sa pravim URI-jem za demo
    sample_uri = "gs://cloud-samples-data/generative-ai/image/landmark.jpg"
    result = analyze_multimodal_content("Explain the architectural style of this building.", sample_uri)
    print(f"Gemini Analysis:\n{result}")
