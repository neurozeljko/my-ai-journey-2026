from vertexai.vision_models import MultiModalEmbeddingModel
from vertexai.generative_models import GenerativeModel

def get_multimodal_embeddings(text=None, image_path=None):
    """
    Generiše vektorske embedinge za tekst ili sliku koristeci Google Multimodal Embedding Model.
    Kljucno za pretrazivanje baze podataka (Vector Search).
    """
    embedding_model = MultiModalEmbeddingModel.from_pretrained("multimodalembedding")
    
    embeddings = embedding_model.get_embeddings(
        image=image_path,
        contextual_text=text
    )
    # Vracamo vektor (listu brojeva)
    return embeddings.embedding

def rag_retrieval_and_answer(user_query, retrieved_context_image):
    """
    Simulira RAG (Retrieval Augmented Generation) proces.
    Uzima korisnicko pitanje i 'pronadjenu' sliku iz baze, pa generise odgovor.
    """
    gen_model = GenerativeModel("gemini-1.0-pro-vision")
    
    prompt = f"""
    Answer the user's question based ONLY on the provided context image.
    User Question: {user_query}
    """
    
    # U realnom sistemu, 'retrieved_context_image' dolazi iz Vector DB pretrage
    response = gen_model.generate_content([retrieved_context_image, prompt])
    return response.text

if __name__ == "__main__":
    print("--- RAG Pipeline Initialized ---")
    # 1. Embed Query
    vector = get_multimodal_embeddings(text="Show me modern chairs")
    print(f"Generated Vector Dimension: {len(vector)}")
