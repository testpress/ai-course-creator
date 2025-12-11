"""Factory for creating AI providers."""

from typing import Optional
from .base_provider import BaseAIProvider
from .openai_provider import OpenAIProvider
from .gemini_provider import GeminiProvider


class ProviderFactory:
    """Factory for creating AI provider instances."""
    
    SUPPORTED_PROVIDERS = {
        "openai": OpenAIProvider,
        "gemini": GeminiProvider
    }
    
    @staticmethod
    def create_provider(
        provider_name: str, 
        api_key: str,
        model: Optional[str] = None
    ) -> BaseAIProvider:
        """
        Create an AI provider instance.
        
        Args:
            provider_name: Name of the provider ('openai' or 'gemini')
            api_key: API key for the provider
            model: Optional model name override
            
        Returns:
            Instance of the requested provider
            
        Raises:
            ValueError: If provider name is not supported
        """
        provider_name = provider_name.lower()
        
        if provider_name not in ProviderFactory.SUPPORTED_PROVIDERS:
            supported = ", ".join(ProviderFactory.SUPPORTED_PROVIDERS.keys())
            raise ValueError(
                f"Unsupported provider: {provider_name}. "
                f"Supported providers: {supported}"
            )
        
        provider_class = ProviderFactory.SUPPORTED_PROVIDERS[provider_name]
        
        if model:
            return provider_class(api_key=api_key, model=model)
        else:
            return provider_class(api_key=api_key)
    
    @staticmethod
    def get_supported_providers() -> list:
        """Get list of supported provider names."""
        return list(ProviderFactory.SUPPORTED_PROVIDERS.keys())
