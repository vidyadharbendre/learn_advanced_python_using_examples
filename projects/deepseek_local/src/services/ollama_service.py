#!/Users/vidyadharbendre/miniforge3/envs/nndl_env/bin/python
import requests
from config import settings

class OllamaService:
    """Handles requests to Ollama API."""
    
    def __init__(self, model_name=settings.MODEL_NAME):
        self.ollama_url = settings.OLLAMA_URL
        self.model_name = model_name

    def generate_response(self, prompt):
        """Send prompt to Ollama model and return response."""
        payload = {"model": self.model_name, "prompt": prompt, "stream": False}
        response = requests.post(self.ollama_url, json=payload)
        return response.json().get("response", "Error: No response received.")