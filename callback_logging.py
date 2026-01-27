from google.genai import types

def log_query_to_model(agent, prompt):
    print(f"--- [LOG] Input to Model ({agent.name}): {prompt}")

def log_model_response(agent, response):
    print(f"--- [LOG] Output from Model ({agent.name}): {response}")
