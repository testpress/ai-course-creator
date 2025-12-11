"""User input collection utilities."""

from ..models.course_input import CourseInput


class InputCollector:
    """Handles collecting user inputs for course generation."""
    
    @staticmethod
    def collect_course_inputs() -> CourseInput:
        """
        Collect user inputs for syllabus generation.
        
        Returns:
            CourseInput object with user's specifications
        """
        print("=" * 60)
        print("AI Course Creator - Syllabus Generator")
        print("=" * 60)
        print()
        
        # Required: Main topic/subject
        topic = input("Enter the course topic/subject: ").strip()
        while not topic:
            print("Topic cannot be empty. Please enter a topic.")
            topic = input("Enter the course topic/subject: ").strip()
        
        # Optional: Complexity level
        print("\nComplexity Level (optional - press Enter to skip):")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        complexity_choice = input("Select complexity (1-3 or Enter to skip): ").strip()
        
        complexity_map = {
            "1": "Beginner",
            "2": "Intermediate",
            "3": "Advanced"
        }
        complexity = complexity_map.get(complexity_choice) if complexity_choice else None
        
        # Optional: Age group
        age_group = input("\nAge group (optional - press Enter to skip): ").strip()
        if not age_group:
            age_group = None
        
        # Optional: Tone/Style
        print("\nTone/Style (optional - press Enter to skip):")
        print("1. Academic")
        print("2. Casual")
        print("3. Professional")
        print("4. Humorous")
        tone_choice = input("Select tone (1-4 or Enter to skip): ").strip()
        
        tone_map = {
            "1": "Academic",
            "2": "Casual",
            "3": "Professional",
            "4": "Humorous"
        }
        tone = tone_map.get(tone_choice) if tone_choice else None
        
        return CourseInput(
            topic=topic,
            complexity=complexity,
            age_group=age_group,
            tone=tone
        )
