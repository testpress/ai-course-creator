"""Display utilities for formatted output."""

from ..models.course_input import CourseInput
from ..models.syllabus import Syllabus


class Display:
    """Handles formatted display of information."""
    
    @staticmethod
    def print_course_inputs(inputs: CourseInput) -> None:
        """
        Print collected user inputs in a formatted way.
        
        Args:
            inputs: CourseInput object to display
        """
        print("\n" + "=" * 60)
        print("Collected Information:")
        print("=" * 60)
        print(inputs)
        print("=" * 60)
    
    @staticmethod
    def print_syllabus(syllabus: Syllabus) -> None:
        """
        Print syllabus in a formatted way.
        
        Args:
            syllabus: Syllabus object to display
        """
        print("\n" + "=" * 60)
        print("Generated Syllabus")
        print("=" * 60)
        print()
        print(syllabus.to_markdown())
        print()
        print("=" * 60)
    
    @staticmethod
    def print_error(message: str) -> None:
        """
        Print error message in a formatted way.
        
        Args:
            message: Error message to display
        """
        print("\n" + "!" * 60)
        print("ERROR:")
        print(message)
        print("!" * 60)
    
    @staticmethod
    def print_success(message: str) -> None:
        """
        Print success message in a formatted way.
        
        Args:
            message: Success message to display
        """
        print("\n" + "✓" * 60)
        print(message)
        print("✓" * 60)
    
    @staticmethod
    def print_info(message: str) -> None:
        """
        Print info message in a formatted way.
        
        Args:
            message: Info message to display
        """
        print(f"\n[INFO] {message}")
