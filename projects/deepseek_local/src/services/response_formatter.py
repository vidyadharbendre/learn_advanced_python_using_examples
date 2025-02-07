import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class ResponseFormatter:
    """Formats the response from Ollama."""
    
    @staticmethod
    def format_text(response):
        return f"🤖 AI says:\n\n{response}"
