"""Syllabus generation service."""

from typing import Dict, Any
from ..models.course_input import CourseInput
from ..models.syllabus import Syllabus, Module, Lesson
from ..providers.base_provider import BaseAIProvider
from ..prompts.syllabus_prompts import SyllabusPromptBuilder


class SyllabusService:
    """Service for generating course syllabi using AI."""
    
    def __init__(self, ai_provider: BaseAIProvider):
        """
        Initialize the syllabus service.
        
        Args:
            ai_provider: AI provider instance to use for generation
        """
        self.ai_provider = ai_provider
        self.prompt_builder = SyllabusPromptBuilder()
    
    def generate_syllabus(self, course_input: CourseInput) -> Syllabus:
        """
        Generate a complete syllabus based on course input.
        
        Args:
            course_input: User's course requirements
            
        Returns:
            Generated Syllabus object
            
        Raises:
            Exception: If generation fails
        """
        # Build prompts
        system_prompt = self.prompt_builder.get_system_prompt()
        user_prompt = self.prompt_builder.build_syllabus_prompt(
            course_input.to_dict()
        )
        
        # Generate using AI provider
        syllabus_data = self.ai_provider.generate_syllabus(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )
        
        # Convert to Syllabus object
        syllabus = self._parse_syllabus_data(syllabus_data)
        
        return syllabus
    
    def _parse_syllabus_data(self, data: Dict[str, Any]) -> Syllabus:
        """
        Parse raw syllabus data into Syllabus object.
        
        Args:
            data: Raw syllabus data from AI
            
        Returns:
            Syllabus object
        """
        # Parse modules
        modules = []
        for module_data in data.get("modules", []):
            # Parse lessons
            lessons = []
            for lesson_data in module_data.get("lessons", []):
                lesson = Lesson(
                    title=lesson_data.get("title", ""),
                    description=lesson_data.get("description"),
                    duration_minutes=lesson_data.get("duration_minutes"),
                    learning_objectives=lesson_data.get("learning_objectives", [])
                )
                lessons.append(lesson)
            
            module = Module(
                title=module_data.get("title", ""),
                description=module_data.get("description"),
                lessons=lessons,
                order=module_data.get("order", 0)
            )
            modules.append(module)
        
        # Create syllabus
        syllabus = Syllabus(
            course_title=data.get("course_title", ""),
            course_description=data.get("course_description", ""),
            target_audience=data.get("target_audience"),
            prerequisites=data.get("prerequisites", []),
            learning_outcomes=data.get("learning_outcomes", []),
            modules=modules,
            total_duration_hours=data.get("total_duration_hours")
        )
        
        return syllabus
