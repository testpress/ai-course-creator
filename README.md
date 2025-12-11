# AI Course Creator

An AI-powered course syllabus generator that uses OpenAI or Google Gemini to create comprehensive, well-structured course outlines.

## Features

- 🎓 **Intelligent Syllabus Generation**: Creates detailed course syllabi with modules, lessons, and learning objectives
- 🔄 **Multiple AI Providers**: Support for both OpenAI (GPT) and Google Gemini
- 📝 **Structured Output**: Generates syllabi in JSON format and exports to Markdown
- 🎯 **Customizable Parameters**: Specify complexity level, age group, and tone/style
- 🏗️ **Modular Architecture**: Clean separation of concerns for easy maintenance and extension

## Project Structure

```
ai-course-creator/
├── src/
│   ├── models/              # Data models
│   │   ├── course_input.py  # User input model
│   │   └── syllabus.py      # Syllabus, Module, Lesson models
│   ├── prompts/             # AI prompt templates
│   │   └── syllabus_prompts.py
│   ├── providers/           # AI provider implementations
│   │   ├── base_provider.py      # Abstract base class
│   │   ├── openai_provider.py    # OpenAI implementation
│   │   ├── gemini_provider.py    # Google Gemini implementation
│   │   └── provider_factory.py   # Provider factory
│   ├── services/            # Business logic
│   │   └── syllabus_service.py
│   ├── utils/               # Utility functions
│   │   ├── input_collector.py
│   │   └── display.py
│   └── config.py            # Configuration management
├── output/                  # Generated syllabi (created automatically)
├── main.py                  # Entry point
├── pyproject.toml          # Project dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## Installation

### Prerequisites

- Python 3.12 or higher
- An API key for either OpenAI or Google Gemini

### Setup

1. **Clone the repository** (or navigate to the project directory)

2. **Install dependencies using uv** (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -e .
   ```

3. **Configure API keys**:
   
   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API key:
   ```env
   # For OpenAI
   AI_PROVIDER=openai
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   
   # OR for Google Gemini
   AI_PROVIDER=gemini
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL=gemini-1.5-flash
   ```

## Usage

### Basic Usage

Run the main script:

```bash
python main.py
```

The program will:
1. Prompt you for course details (topic, complexity, age group, tone)
2. Generate a comprehensive syllabus using AI
3. Display the syllabus in the terminal
4. Save it as a Markdown file in the `output/` directory

### Example Session

```
============================================================
AI Course Creator - Syllabus Generator
============================================================

Enter the course topic/subject: Python Programming

Complexity Level (optional - press Enter to skip):
1. Beginner
2. Intermediate
3. Advanced
Select complexity (1-3 or Enter to skip): 1

Age group (optional - press Enter to skip): Adults

Tone/Style (optional - press Enter to skip):
1. Academic
2. Casual
3. Professional
4. Humorous
Select tone (1-4 or Enter to skip): 3

[INFO] Setting up AI provider...
[INFO] Using OPENAI with model gpt-4o-mini
[INFO] Validating API key...
[INFO] Generating syllabus... This may take a moment.

============================================================
Generated Syllabus
============================================================
[Syllabus content displayed here]
============================================================

✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓
Syllabus saved to: output/python_programming_syllabus.md
✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓
```

## Architecture

### Separation of Concerns

The project follows a clean architecture with clear separation:

1. **Models** (`src/models/`): Data structures for course inputs and syllabus components
2. **Prompts** (`src/prompts/`): AI prompt templates and builders
3. **Providers** (`src/providers/`): AI provider implementations with a common interface
4. **Services** (`src/services/`): Business logic for syllabus generation
5. **Utils** (`src/utils/`): Helper functions for I/O and display
6. **Config** (`src/config.py`): Configuration and environment management

### AI Provider Abstraction

The system uses a provider pattern to support multiple AI services:

```python
# All providers implement the BaseAIProvider interface
class BaseAIProvider(ABC):
    def generate_syllabus(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        pass
```

This makes it easy to:
- Switch between providers
- Add new providers
- Test with mock providers

### Data Flow

1. **Input Collection** → `CourseInput` model
2. **Prompt Building** → Structured prompts from templates
3. **AI Generation** → Provider generates JSON response
4. **Data Parsing** → Convert JSON to `Syllabus` model
5. **Output** → Display and save as Markdown

## API Response Format

The AI providers return JSON in this structure:

```json
{
  "course_title": "Course Title",
  "course_description": "Description",
  "target_audience": "Target audience",
  "prerequisites": ["Prerequisite 1", "Prerequisite 2"],
  "learning_outcomes": ["Outcome 1", "Outcome 2"],
  "total_duration_hours": 40,
  "modules": [
    {
      "title": "Module Title",
      "description": "Module description",
      "order": 1,
      "lessons": [
        {
          "title": "Lesson Title",
          "description": "Lesson description",
          "duration_minutes": 60,
          "learning_objectives": ["Objective 1", "Objective 2"]
        }
      ]
    }
  ]
}
```

## Programmatic Usage

You can also use the components programmatically:

```python
from src.config import Config
from src.models.course_input import CourseInput
from src.providers import ProviderFactory
from src.services import SyllabusService

# Setup
config = Config.from_env()
provider = ProviderFactory.create_provider("openai", api_key="your-key")
service = SyllabusService(ai_provider=provider)

# Generate syllabus
course_input = CourseInput(
    topic="Machine Learning",
    complexity="Intermediate",
    age_group="College students",
    tone="Academic"
)

syllabus = service.generate_syllabus(course_input)

# Access the syllabus
print(syllabus.course_title)
print(syllabus.to_markdown())

# The syllabus variable contains the complete structured data
for module in syllabus.modules:
    print(f"Module: {module.title}")
    for lesson in module.lessons:
        print(f"  - {lesson.title}")
```

## Configuration

### Environment Variables

- `AI_PROVIDER`: Choose 'openai' or 'gemini' (default: 'openai')
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: OpenAI model to use (default: 'gpt-4o-mini')
- `GEMINI_API_KEY`: Your Google Gemini API key
- `GEMINI_MODEL`: Gemini model to use (default: 'gemini-1.5-flash')

### Supported Models

**OpenAI:**
- `gpt-4o-mini` (default, cost-effective)
- `gpt-4o`
- `gpt-4-turbo`
- `gpt-3.5-turbo`

**Google Gemini:**
- `gemini-1.5-flash` (default, fast and efficient)
- `gemini-1.5-pro`
- `gemini-pro`

## Extending the System

### Adding a New AI Provider

1. Create a new provider class in `src/providers/`:

```python
from .base_provider import BaseAIProvider

class NewProvider(BaseAIProvider):
    def generate_syllabus(self, system_prompt: str, user_prompt: str):
        # Implementation
        pass
    
    def validate_api_key(self):
        # Implementation
        pass
```

2. Register it in `provider_factory.py`:

```python
SUPPORTED_PROVIDERS = {
    "openai": OpenAIProvider,
    "gemini": GeminiProvider,
    "newprovider": NewProvider  # Add here
}
```

### Adding New Prompt Templates

Create new prompt builders in `src/prompts/` following the pattern in `syllabus_prompts.py`.

## Troubleshooting

### API Key Issues

If you get API key errors:
1. Check that your `.env` file exists and has the correct key
2. Verify the key is valid by testing it directly with the provider
3. Ensure you've selected the correct provider in `.env`

### Import Errors

If you get import errors:
```bash
# Reinstall dependencies
uv sync
# Or
pip install -e .
```

### JSON Parsing Errors

If the AI returns invalid JSON:
- Try a different model (e.g., switch from gpt-4o-mini to gpt-4o)
- Check your prompt in `src/prompts/syllabus_prompts.py`
- The providers are configured to request JSON format responses

## Future Enhancements

- [ ] Web interface (FastAPI + React)
- [ ] Database storage for generated syllabi
- [ ] Content generation for individual lessons
- [ ] Quiz and assessment generation
- [ ] Export to multiple formats (PDF, SCORM, etc.)
- [ ] Template system for different course types
- [ ] Collaborative editing features

## License

This project is part of the AI Course Creator initiative.

## Contributing

Contributions are welcome! Please ensure:
- Code follows the existing architecture
- New providers implement `BaseAIProvider`
- Models are properly typed with dataclasses
- Functions have clear docstrings
