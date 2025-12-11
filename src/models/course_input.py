"""Course input data model."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CourseInput:
    """User input for course generation."""
    
    topic: str
    complexity: Optional[str] = None
    age_group: Optional[str] = None
    tone: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary format."""
        return {
            "topic": self.topic,
            "complexity": self.complexity,
            "age_group": self.age_group,
            "tone": self.tone
        }
    
    def __str__(self) -> str:
        """String representation for display."""
        lines = [
            f"Topic/Subject: {self.topic}",
            f"Complexity: {self.complexity or 'Not specified'}",
            f"Age Group: {self.age_group or 'Not specified'}",
            f"Tone/Style: {self.tone or 'Not specified'}"
        ]
        return "\n".join(lines)
