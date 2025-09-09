#!/usr/bin/env python3
"""
OpenAI API Adapter - Convert Azure OpenAI calls to regular OpenAI API
"""

import os
from typing import List, Dict, Any
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OpenAIAdapter:
    """Adapter to use regular OpenAI API instead of Azure OpenAI"""
    
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        
    def get_chat_completions(self, model: str, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Convert Azure OpenAI chat completions to regular OpenAI format
        """
        # Map Azure model names to OpenAI model names
        model_mapping = {
            "hackmerlin-gpt35": "gpt-3.5-turbo",
            "hackmerlin-gpt4": "gpt-4",
            "gpt-35-turbo": "gpt-3.5-turbo",
            "gpt-4": "gpt-4"
        }
        
        openai_model = model_mapping.get(model, "gpt-3.5-turbo")
        
        # Convert Azure message format to OpenAI format
        openai_messages = []
        for msg in messages:
            if hasattr(msg, 'role') and hasattr(msg, 'content'):
                # Azure ChatRequestMessage format
                openai_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
            elif isinstance(msg, dict):
                # Already in dict format
                openai_messages.append(msg)
        
        try:
            response = self.client.chat.completions.create(
                model=openai_model,
                messages=openai_messages,
                max_tokens=200,
                temperature=0.2
            )
            
            # Convert response to Azure format
            azure_response = {
                "choices": [{
                    "message": {
                        "content": response.choices[0].message.content
                    }
                }]
            }
            
            return azure_response
            
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            # Return empty response on error
            return {
                "choices": [{
                    "message": {
                        "content": "I cannot help with that."
                    }
                }]
            }

# Environment variable configuration
def get_openai_client():
    """Get OpenAI client with API key from environment"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    
    return OpenAIAdapter(api_key)

# Usage example:
if __name__ == "__main__":
    # Set your OpenAI API key
    os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"
    
    client = get_openai_client()
    
    # Test the adapter
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    
    response = client.get_chat_completions("gpt-3.5-turbo", messages)
    print(response["choices"][0]["message"]["content"]) 