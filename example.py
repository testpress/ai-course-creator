"""Example script demonstrating programmatic usage of the AI Course Creator."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.config import Config
from src.models.course_input import CourseInput
from src.providers import ProviderFactory
from src.services import SyllabusService
from src.utils import Display


def example_basic_usage():
    """Example: Basic syllabus generation."""
    print("\n" + "=" * 60)
    print("Example 1: Basic Syllabus Generation")
    print("=" * 60)
    
    # Load configuration
    config = Config.from_env()
    
    # Get API key
    api_key = config.get_api_key()
    if not api_key:
        print("Error: No API key found. Please set up your .env file.")
        return
    
    # Create provider
    provider = ProviderFactory.create_provider(
        provider_name=config.ai_provider,
        api_key=api_key,
        model=config.get_model()
    )
    
    # Create service
    service = SyllabusService(ai_provider=provider)
    
    # Create course input
    course_input = CourseInput(
        topic="Introduction to Web Development",
        complexity="Beginner",
        age_group="High school students",
        tone="Casual"
    )
    
    print(f"\nGenerating syllabus for: {course_input.topic}")
    print("This may take a moment...\n")
    
    # Generate syllabus
    syllabus = service.generate_syllabus(course_input)
    
    # Display results
    print(f"Course Title: {syllabus.course_title}")
    print(f"Total Modules: {len(syllabus.modules)}")
    print(f"Total Duration: {syllabus.total_duration_hours} hours")
    print(f"\nFirst module: {syllabus.modules[0].title}")
    print(f"Lessons in first module: {len(syllabus.modules[0].lessons)}")
    
    return syllabus


def example_accessing_syllabus_data():
    """Example: Accessing syllabus data programmatically."""
    print("\n" + "=" * 60)
    print("Example 2: Accessing Syllabus Data")
    print("=" * 60)
    
    config = Config.from_env()
    api_key = config.get_api_key()
    
    if not api_key:
        print("Error: No API key found.")
        return
    
    provider = ProviderFactory.create_provider(
        provider_name=config.ai_provider,
        api_key=api_key
    )
    
    service = SyllabusService(ai_provider=provider)
    
    course_input = CourseInput(
        topic="Data Science Fundamentals",
        complexity="Intermediate"
    )
    
    print(f"\nGenerating syllabus for: {course_input.topic}\n")
    syllabus = service.generate_syllabus(course_input)
    
    # Access syllabus data
    print("Course Structure:")
    print(f"Title: {syllabus.course_title}")
    print(f"Description: {syllabus.course_description[:100]}...")
    print(f"\nLearning Outcomes:")
    for i, outcome in enumerate(syllabus.learning_outcomes, 1):
        print(f"  {i}. {outcome}")
    
    print(f"\nModules and Lessons:")
    for module_idx, module in enumerate(syllabus.modules, 1):
        print(f"\n  Module {module_idx}: {module.title}")
        for lesson_idx, lesson in enumerate(module.lessons, 1):
            duration = f" ({lesson.duration_minutes} min)" if lesson.duration_minutes else ""
            print(f"    {lesson_idx}. {lesson.title}{duration}")
    
    # Export to markdown
    markdown_content = syllabus.to_markdown()
    print(f"\nMarkdown length: {len(markdown_content)} characters")
    
    return syllabus


def example_multiple_providers():
    """Example: Comparing different AI providers."""
    print("\n" + "=" * 60)
    print("Example 3: Using Different Providers")
    print("=" * 60)
    
    config = Config.from_env()
    
    course_input = CourseInput(
        topic="Python Programming Basics",
        complexity="Beginner"
    )
    
    # Try OpenAI if available
    if config.openai_api_key:
        print("\n--- Using OpenAI ---")
        openai_provider = ProviderFactory.create_provider(
            provider_name="openai",
            api_key=config.openai_api_key,
            model="gpt-4o-mini"
        )
        service = SyllabusService(ai_provider=openai_provider)
        syllabus = service.generate_syllabus(course_input)
        print(f"Generated: {syllabus.course_title}")
        print(f"Modules: {len(syllabus.modules)}")
    
    # Try Gemini if available
    if config.gemini_api_key:
        print("\n--- Using Google Gemini ---")
        gemini_provider = ProviderFactory.create_provider(
            provider_name="gemini",
            api_key=config.gemini_api_key,
            model="gemini-1.5-flash"
        )
        service = SyllabusService(ai_provider=gemini_provider)
        syllabus = service.generate_syllabus(course_input)
        print(f"Generated: {syllabus.course_title}")
        print(f"Modules: {len(syllabus.modules)}")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("AI Course Creator - Programmatic Usage Examples")
    print("=" * 60)
    
    try:
        # Example 1: Basic usage
        syllabus1 = example_basic_usage()
        
        # Example 2: Accessing data
        # syllabus2 = example_accessing_syllabus_data()
        
        # Example 3: Multiple providers
        # example_multiple_providers()
        
        print("\n" + "=" * 60)
        print("Examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        Display.print_error(f"Error running examples: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
