"""Google Gemini provider implementation."""

import json
from typing import Dict, Any
from .base_provider import BaseAIProvider


class GeminiProvider(BaseAIProvider):
    """Google Gemini API provider for syllabus generation."""
    
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash"):
        """
        Initialize Gemini provider.
        
        Args:
            api_key: Google API key
            model: Model to use (default: gemini-1.5-flash)
        """
        super().__init__(api_key)
        self.model = model
        self._client = None
    
    def _get_client(self):
        """Lazy load the Gemini client."""
        if self._client is None:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self._client = genai.GenerativeModel(
                    model_name=self.model,
                    generation_config={
                        "temperature": 0.7,
                        "max_output_tokens": 8192,
                        "response_mime_type": "application/json"
                    }
                )
            except ImportError:
                raise ImportError(
                    "Google Generative AI package not installed. "
                    "Install it with: pip install google-generativeai"
                )
        return self._client
    
    def generate_syllabus(
        self, 
        system_prompt: str, 
        user_prompt: str
    ) -> Dict[str, Any]:
        """
        Generate syllabus using Gemini API.
        
        Args:
            system_prompt: System instructions
            user_prompt: User request
            
        Returns:
            Dictionary with syllabus data
        """
        client = self._get_client()
        
        # Combine system and user prompts for Gemini
        combined_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        try:
            response = client.generate_content(combined_prompt)
            
            # Extract text from response
            content = response.text
            
            # Parse JSON
            syllabus_data = json.loads(content)
            
            return syllabus_data
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON response: {e}")
        except Exception as e:
            raise Exception(f"Gemini API error: {e}")
    
    def validate_api_key(self) -> bool:
        """
        Validate Gemini API key.
        
        Returns:
            True if valid, False otherwise
        """
        try:
            client = self._get_client()
            # Make a minimal API call to test the key
            test_response = client.generate_content("Test")
            return test_response is not None
        except Exception:
            return False
