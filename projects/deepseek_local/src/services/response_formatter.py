class ResponseFormatter:
    """Formats the response from Ollama."""
    
    @staticmethod
    def format_text(response):
        return f"🤖 AI says:\n\n{response}"
