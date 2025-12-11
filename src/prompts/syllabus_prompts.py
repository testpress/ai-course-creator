"""Prompt templates for syllabus generation."""

from typing import Dict, Any


class SyllabusPromptBuilder:
    """Builds prompts for syllabus generation based on user inputs."""
    
    SYSTEM_PROMPT = """You are an expert curriculum designer and educational content creator. 
Your task is to create comprehensive, well-structured course syllabi that are pedagogically sound 
and engaging for learners. You should consider learning theory, proper pacing, and clear learning objectives.

Always respond with valid JSON following the exact schema provided."""
    
    @staticmethod
    def build_syllabus_prompt(course_input: Dict[str, Any]) -> str:
        """
        Build a detailed prompt for syllabus generation.
        
        Args:
            course_input: Dictionary containing topic, complexity, age_group, and tone
            
        Returns:
            Formatted prompt string
        """
        topic = course_input.get("topic", "")
        complexity = course_input.get("complexity")
        age_group = course_input.get("age_group")
        tone = course_input.get("tone")
        
        # Build the base prompt
        prompt_parts = [
            f"Create a comprehensive course syllabus for the topic: **{topic}**",
            ""
        ]
        
        # Add optional parameters
        if complexity:
            prompt_parts.append(f"- **Complexity Level**: {complexity}")
        
        if age_group:
            prompt_parts.append(f"- **Target Age Group**: {age_group}")
        
        if tone:
            prompt_parts.append(f"- **Tone/Style**: {tone}")
        
        if complexity or age_group or tone:
            prompt_parts.append("")
        
        # Add detailed requirements
        prompt_parts.extend([
            "## Requirements:",
            "",
            "1. Create a well-structured syllabus with 4-8 modules",
            "2. Each module should have 3-6 lessons",
            "3. Include clear learning objectives for each lesson",
            "4. Provide estimated duration for each lesson (in minutes)",
            "5. Include course description, target audience, prerequisites, and overall learning outcomes",
            "6. Ensure logical progression from basic to advanced concepts",
            "7. Make the content engaging and appropriate for the specified audience",
            "",
            "## JSON Schema:",
            "",
            "Respond with a JSON object following this exact structure:",
            "",
            "```json",
            "{",
            '  "course_title": "string",',
            '  "course_description": "string",',
            '  "target_audience": "string",',
            '  "prerequisites": ["string"],',
            '  "learning_outcomes": ["string"],',
            '  "total_duration_hours": number,',
            '  "modules": [',
            "    {",
            '      "title": "string",',
            '      "description": "string",',
            '      "order": number,',
            '      "lessons": [',
            "        {",
            '          "title": "string",',
            '          "description": "string",',
            '          "duration_minutes": number,',
            '          "learning_objectives": ["string"]',
            "        }",
            "      ]",
            "    }",
            "  ]",
            "}",
            "```",
            "",
            "Provide ONLY the JSON response, no additional text or markdown formatting."
        ])
        
        return "\n".join(prompt_parts)
    
    @staticmethod
    def get_system_prompt() -> str:
        """Get the system prompt for the AI model."""
        return SyllabusPromptBuilder.SYSTEM_PROMPT
