"""Configuration management for the application."""

import os
from typing import Optional
from dataclasses import dataclass
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    # Load .env from project root
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    # python-dotenv not installed, skip
    pass


@dataclass
class Config:
    """Application configuration."""
    
    # AI Provider settings
    ai_provider: str = "openai"  # 'openai' or 'gemini'
    openai_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    openai_model: str = "gpt-4o-mini"
    gemini_model: str = "gemini-1.5-flash"
    
    @classmethod
    def from_env(cls) -> "Config":
        """
        Load configuration from environment variables.
        
        Returns:
            Config instance
        """
        return cls(
            ai_provider=os.getenv("AI_PROVIDER", "openai"),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            gemini_api_key=os.getenv("GEMINI_API_KEY"),
            openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            gemini_model=os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        )
    
    def get_api_key(self, provider: Optional[str] = None) -> Optional[str]:
        """
        Get API key for the specified provider.
        
        Args:
            provider: Provider name (defaults to configured provider)
            
        Returns:
            API key or None
        """
        provider = provider or self.ai_provider
        
        if provider == "openai":
            return self.openai_api_key
        elif provider == "gemini":
            return self.gemini_api_key
        
        return None
    
    def get_model(self, provider: Optional[str] = None) -> str:
        """
        Get model name for the specified provider.
        
        Args:
            provider: Provider name (defaults to configured provider)
            
        Returns:
            Model name
        """
        provider = provider or self.ai_provider
        
        if provider == "openai":
            return self.openai_model
        elif provider == "gemini":
            return self.gemini_model
        
        return ""
