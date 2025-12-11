"""Base AI provider interface."""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAIProvider(ABC):
    """Abstract base class for AI providers."""
    
    def __init__(self, api_key: str):
        """
        Initialize the provider with API key.
        
        Args:
            api_key: API key for the provider
        """
        self.api_key = api_key
    
    @abstractmethod
    def generate_syllabus(
        self, 
        system_prompt: str, 
        user_prompt: str
    ) -> Dict[str, Any]:
        """
        Generate a syllabus using the AI provider.
        
        Args:
            system_prompt: System-level instructions for the AI
            user_prompt: User's specific request
            
        Returns:
            Dictionary containing the generated syllabus data
            
        Raises:
            Exception: If generation fails
        """
        pass
    
    @abstractmethod
    def validate_api_key(self) -> bool:
        """
        Validate that the API key is working.
        
        Returns:
            True if API key is valid, False otherwise
        """
        pass
