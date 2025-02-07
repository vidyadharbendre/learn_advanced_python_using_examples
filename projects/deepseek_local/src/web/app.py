import streamlit as st
from src.services.ollama_service import OllamaService
from src.services.response_formatter import ResponseFormatter

# Initialize the service
ollama_service = OllamaService()

# Streamlit UI
st.title("Chat with DeepSeek 8B (Local) 🤖")
user_input = st.text_area("Enter your message:", "")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            response = ollama_service.generate_response(user_input)
            formatted_response = ResponseFormatter.format_text(response)
        st.text_area("DeepSeek's Response:", formatted_response, height=200)
    else:
        st.warning("Please enter a message.")
