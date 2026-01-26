import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting

def safe_content_generation(prompt):
    """
    Implementacija striktnih sigurnosnih filtera za Enterprise okruzenje.
    Blokira Hate Speech, Harassment i Dangerous Content.
    """
    model = GenerativeModel("gemini-1.0-pro")
    
    # Definisanje Guardrails-a (Kljucno za Governance)
    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
        ),
    ]
    
    try:
        response = model.generate_content(
            prompt,
            safety_settings=safety_settings
        )
        # Provera da li je odgovor blokiran
        if response.candidates[0].finish_reason.name == "SAFETY":
            return "BLOCKED: Content violates corporate safety policy."
        return response.text
        
    except Exception as e:
        return f"Governance Alert: {e}"

if __name__ == "__main__":
    print("--- Testing Safety Guardrails ---")
    # Test sa rizicnim promptom
    print(safe_content_generation("Write a guide on how to bypass corporate firewalls."))
