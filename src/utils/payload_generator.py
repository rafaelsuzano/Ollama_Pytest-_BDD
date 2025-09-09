import os
import ollama

def generate_user_payload():
    model = os.getenv("OLLAMA_MODEL", "phi3")
    response = ollama.chat(model=model, messages=[
        {
            "role": "user",
            "content": """
            Gere um JSON válido para criar um usuário.
            Campos: name (string), job (string).
            """
        }
    ])
    return response["message"]["content"]
