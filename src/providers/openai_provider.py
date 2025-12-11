"""OpenAI provider implementation."""

import json
from typing import Dict, Any
from .base_provider import BaseAIProvider


class OpenAIProvider(BaseAIProvider):
    """OpenAI API provider for syllabus generation."""
    
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        """
        Initialize OpenAI provider.
        
        Args:
            api_key: OpenAI API key
            model: Model to use (default: gpt-4o-mini)
        """
        super().__init__(api_key)
        self.model = model
        self._client = None
    
    def _get_client(self):
        """Lazy load the OpenAI client."""
        if self._client is None:
            try:
                from openai import OpenAI
                self._client = OpenAI(api_key=self.api_key)
            except ImportError:
                raise ImportError(
                    "OpenAI package not installed. "
                    "Install it with: pip install openai"
                )
        return self._client
    
    def generate_syllabus(
        self, 
        system_prompt: str, 
        user_prompt: str
    ) -> Dict[str, Any]:
        """
        Generate syllabus using OpenAI API.
        
        Args:
            system_prompt: System instructions
            user_prompt: User request
            
        Returns:
            Dictionary with syllabus data
        """
        client = self._get_client()
        
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.7,
                max_tokens=4000
            )
            
            content = response.choices[0].message.content
            syllabus_data = json.loads(content)
            
            return syllabus_data
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON response: {e}")
        except Exception as e:
            raise Exception(f"OpenAI API error: {e}")
    
    def validate_api_key(self) -> bool:
        """
        Validate OpenAI API key.
        
        Returns:
            True if valid, False otherwise
        """
        try:
            client = self._get_client()
            # Make a minimal API call to test the key
            client.models.list()
            return True
        except Exception:
            return False
