"""Syllabus data models."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Lesson:
    """Represents a single lesson within a module."""
    
    title: str
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    learning_objectives: List[str] = field(default_factory=list)


@dataclass
class Module:
    """Represents a module/section in the course."""
    
    title: str
    description: Optional[str] = None
    lessons: List[Lesson] = field(default_factory=list)
    order: int = 0


@dataclass
class Syllabus:
    """Complete course syllabus structure."""
    
    course_title: str
    course_description: str
    target_audience: Optional[str] = None
    prerequisites: List[str] = field(default_factory=list)
    learning_outcomes: List[str] = field(default_factory=list)
    modules: List[Module] = field(default_factory=list)
    total_duration_hours: Optional[float] = None
    
    def to_markdown(self) -> str:
        """Convert syllabus to markdown format."""
        md_lines = [
            f"# {self.course_title}",
            "",
            "## Course Description",
            self.course_description,
            ""
        ]
        
        if self.target_audience:
            md_lines.extend([
                "## Target Audience",
                self.target_audience,
                ""
            ])
        
        if self.prerequisites:
            md_lines.extend([
                "## Prerequisites",
                *[f"- {prereq}" for prereq in self.prerequisites],
                ""
            ])
        
        if self.learning_outcomes:
            md_lines.extend([
                "## Learning Outcomes",
                *[f"- {outcome}" for outcome in self.learning_outcomes],
                ""
            ])
        
        if self.total_duration_hours:
            md_lines.extend([
                f"## Total Duration: {self.total_duration_hours} hours",
                ""
            ])
        
        md_lines.append("## Course Modules")
        md_lines.append("")
        
        for idx, module in enumerate(self.modules, 1):
            md_lines.extend([
                f"### Module {idx}: {module.title}",
                ""
            ])
            
            if module.description:
                md_lines.extend([
                    module.description,
                    ""
                ])
            
            if module.lessons:
                md_lines.append("**Lessons:**")
                for lesson_idx, lesson in enumerate(module.lessons, 1):
                    duration = f" ({lesson.duration_minutes} min)" if lesson.duration_minutes else ""
                    md_lines.append(f"{lesson_idx}. {lesson.title}{duration}")
                    
                    if lesson.description:
                        md_lines.append(f"   - {lesson.description}")
                    
                    if lesson.learning_objectives:
                        md_lines.append("   - Learning Objectives:")
                        for obj in lesson.learning_objectives:
                            md_lines.append(f"     - {obj}")
                
                md_lines.append("")
        
        return "\n".join(md_lines)
