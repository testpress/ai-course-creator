"""AI Course Creator - Main Entry Point."""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.config import Config
from src.models.syllabus import Syllabus
from src.providers import ProviderFactory
from src.services import SyllabusService
from src.utils import InputCollector, Display


def setup_api_keys(config: Config) -> tuple[str, str]:
    """
    Setup and validate API keys.
    
    Args:
        config: Configuration object
        
    Returns:
        Tuple of (provider_name, api_key)
    """
    # Check if API keys are available
    openai_key = config.openai_api_key
    gemini_key = config.gemini_api_key
    
    # If no keys in environment, prompt user
    if not openai_key and not gemini_key:
        Display.print_info("No API keys found in environment variables.")
        print("\nPlease select an AI provider:")
        print("1. OpenAI (GPT)")
        print("2. Google Gemini")
        
        choice = input("\nSelect provider (1-2): ").strip()
        
        if choice == "1":
            provider = "openai"
            api_key = input("Enter your OpenAI API key: ").strip()
        elif choice == "2":
            provider = "gemini"
            api_key = input("Enter your Google Gemini API key: ").strip()
        else:
            raise ValueError("Invalid provider selection")
    else:
        # Use configured provider
        provider = config.ai_provider
        api_key = config.get_api_key(provider)
        
        if not api_key:
            # Try the other provider
            if provider == "openai" and gemini_key:
                provider = "gemini"
                api_key = gemini_key
            elif provider == "gemini" and openai_key:
                provider = "openai"
                api_key = openai_key
            else:
                raise ValueError(f"No API key found for {provider}")
    
    return provider, api_key


def save_syllabus(syllabus: Syllabus, output_dir: str = "output") -> str:
    """
    Save syllabus to a markdown file.
    
    Args:
        syllabus: Syllabus object to save
        output_dir: Directory to save the file
        
    Returns:
        Path to saved file
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)
    
    # Generate filename from course title
    filename = syllabus.course_title.lower()
    filename = "".join(c if c.isalnum() or c.isspace() else "" for c in filename)
    filename = "_".join(filename.split()) + "_syllabus.md"
    
    filepath = Path(output_dir) / filename
    
    # Write markdown content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(syllabus.to_markdown())
    
    return str(filepath)


def main():
    """Main function to run the syllabus generator."""
    try:
        # Load configuration
        config = Config.from_env()
        
        # Collect user inputs
        course_input = InputCollector.collect_course_inputs()
        Display.print_course_inputs(course_input)
        
        # Setup API provider
        Display.print_info("Setting up AI provider...")
        provider_name, api_key = setup_api_keys(config)
        model = config.get_model(provider_name)
        
        # Create provider instance
        Display.print_info(f"Using {provider_name.upper()} with model {model}")
        provider = ProviderFactory.create_provider(
            provider_name=provider_name,
            api_key=api_key,
            model=model
        )
        
        # Validate API key
        Display.print_info("Validating API key...")
        if not provider.validate_api_key():
            Display.print_error("Invalid API key. Please check your credentials.")
            return
        
        # Create syllabus service
        syllabus_service = SyllabusService(ai_provider=provider)
        
        # Generate syllabus
        Display.print_info("Generating syllabus... This may take a moment.")
        syllabus = syllabus_service.generate_syllabus(course_input)
        
        # Display syllabus
        Display.print_syllabus(syllabus)
        
        # Save to file
        output_path = save_syllabus(syllabus)
        Display.print_success(f"Syllabus saved to: {output_path}")
        
        # Store syllabus in a variable (as requested)
        # The syllabus is already in the 'syllabus' variable
        # It can be accessed as:
        # - syllabus.to_markdown() for markdown format
        # - syllabus object for programmatic access
        
        return syllabus
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        Display.print_error(f"An error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    generated_syllabus = main()
