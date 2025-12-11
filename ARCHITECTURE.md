# AI Course Creator - Architecture Documentation

## Overview

The AI Course Creator is organized into a modular architecture with clear separation of concerns. This document provides a detailed overview of the system architecture and data flow.

## Module Organization

### 1. Models (`src/models/`)

**Purpose**: Define data structures for the application

- **`course_input.py`**: User input data model
  - `CourseInput`: Encapsulates topic, complexity, age_group, and tone
  - Methods: `to_dict()`, `__str__()`

- **`syllabus.py`**: Syllabus structure models
  - `Lesson`: Individual lesson with title, description, duration, learning objectives
  - `Module`: Collection of lessons with title and description
  - `Syllabus`: Complete course structure with metadata
  - Methods: `to_markdown()` for export

### 2. Prompts (`src/prompts/`)

**Purpose**: Manage AI prompt templates

- **`syllabus_prompts.py`**: Prompt builder for syllabus generation
  - `SyllabusPromptBuilder`: Constructs prompts based on user input
  - `SYSTEM_PROMPT`: Expert curriculum designer persona
  - `build_syllabus_prompt()`: Creates detailed user prompts with JSON schema
  - `get_system_prompt()`: Returns system-level instructions

### 3. Providers (`src/providers/`)

**Purpose**: Abstract AI provider implementations

- **`base_provider.py`**: Abstract base class
  - `BaseAIProvider`: Interface for all providers
  - Methods: `generate_syllabus()`, `validate_api_key()`

- **`openai_provider.py`**: OpenAI implementation
  - Uses OpenAI Chat Completions API
  - Supports JSON mode for structured output
  - Default model: `gpt-4o-mini`

- **`gemini_provider.py`**: Google Gemini implementation
  - Uses Google Generative AI SDK
  - Configured for JSON response format
  - Default model: `gemini-1.5-flash`

- **`provider_factory.py`**: Factory pattern
  - `ProviderFactory`: Creates provider instances
  - `create_provider()`: Factory method
  - `get_supported_providers()`: Lists available providers

### 4. Services (`src/services/`)

**Purpose**: Business logic and orchestration

- **`syllabus_service.py`**: Syllabus generation service
  - `SyllabusService`: Orchestrates the generation process
  - `generate_syllabus()`: Main generation method
  - `_parse_syllabus_data()`: Converts JSON to Syllabus objects

### 5. Utils (`src/utils/`)

**Purpose**: Helper functions and utilities

- **`input_collector.py`**: User input collection
  - `InputCollector`: Handles interactive user input
  - `collect_course_inputs()`: Prompts user for course details

- **`display.py`**: Formatted output
  - `Display`: Handles all console output
  - Methods: `print_course_inputs()`, `print_syllabus()`, `print_error()`, etc.

### 6. Configuration (`src/config.py`)

**Purpose**: Application configuration management

- **`Config`**: Configuration dataclass
  - Loads from environment variables
  - Manages API keys for multiple providers
  - `from_env()`: Factory method to load from environment
  - `get_api_key()`: Retrieves API key for provider
  - `get_model()`: Retrieves model name for provider

## Data Flow

```
1. User Input
   ↓
2. InputCollector.collect_course_inputs()
   ↓
3. CourseInput (model)
   ↓
4. SyllabusPromptBuilder.build_syllabus_prompt()
   ↓
5. AI Provider (OpenAI/Gemini)
   ↓
6. JSON Response
   ↓
7. SyllabusService._parse_syllabus_data()
   ↓
8. Syllabus (model)
   ↓
9. Display.print_syllabus() + Save to file
```

## Key Design Patterns

### 1. **Factory Pattern** (Provider Creation)
```python
provider = ProviderFactory.create_provider(
    provider_name="openai",
    api_key="...",
    model="gpt-4o-mini"
)
```

### 2. **Strategy Pattern** (AI Providers)
Different AI providers implement the same interface, allowing runtime selection:
```python
class BaseAIProvider(ABC):
    def generate_syllabus(self, system_prompt, user_prompt):
        pass
```

### 3. **Builder Pattern** (Prompt Construction)
```python
prompt_builder = SyllabusPromptBuilder()
prompt = prompt_builder.build_syllabus_prompt(course_input.to_dict())
```

### 4. **Service Layer Pattern** (Business Logic)
```python
service = SyllabusService(ai_provider=provider)
syllabus = service.generate_syllabus(course_input)
```

## JSON Schema

The AI providers return structured JSON following this schema:

```json
{
  "course_title": "string",
  "course_description": "string",
  "target_audience": "string",
  "prerequisites": ["string"],
  "learning_outcomes": ["string"],
  "total_duration_hours": number,
  "modules": [
    {
      "title": "string",
      "description": "string",
      "order": number,
      "lessons": [
        {
          "title": "string",
          "description": "string",
          "duration_minutes": number,
          "learning_objectives": ["string"]
        }
      ]
    }
  ]
}
```

## Extension Points

### Adding a New AI Provider

1. Create new provider class inheriting from `BaseAIProvider`
2. Implement `generate_syllabus()` and `validate_api_key()`
3. Register in `ProviderFactory.SUPPORTED_PROVIDERS`
4. Add configuration in `Config` class

### Adding New Prompt Types

1. Create new prompt builder in `src/prompts/`
2. Follow the pattern in `SyllabusPromptBuilder`
3. Define system prompt and user prompt builder
4. Include JSON schema in prompt

### Adding New Models

1. Create dataclass in `src/models/`
2. Add conversion methods (`to_dict()`, `to_markdown()`, etc.)
3. Update services to use new models

## Error Handling

- **API Key Validation**: Providers validate keys before generation
- **JSON Parsing**: Robust error handling for malformed responses
- **User Input**: Validation of required fields
- **Environment**: Graceful fallback if `.env` not found

## Configuration Hierarchy

1. Environment variables (`.env` file)
2. Runtime configuration (passed to functions)
3. Default values (hardcoded in `Config` class)

## Testing Strategy

### Unit Tests
- Test individual components (models, prompts, providers)
- Mock AI provider responses
- Validate data transformations

### Integration Tests
- Test end-to-end flow
- Use test API keys or mock providers
- Validate file output

### Example Test Structure
```python
def test_syllabus_generation():
    # Arrange
    mock_provider = MockAIProvider()
    service = SyllabusService(ai_provider=mock_provider)
    course_input = CourseInput(topic="Test")
    
    # Act
    syllabus = service.generate_syllabus(course_input)
    
    # Assert
    assert syllabus.course_title is not None
    assert len(syllabus.modules) > 0
```

## Performance Considerations

- **Lazy Loading**: AI clients are initialized only when needed
- **Caching**: Consider caching generated syllabi
- **Async Support**: Future enhancement for concurrent generation
- **Rate Limiting**: Respect API provider rate limits

## Security Considerations

- **API Keys**: Never commit `.env` files
- **Input Validation**: Sanitize user inputs
- **Error Messages**: Don't expose API keys in error messages
- **Dependencies**: Keep AI provider SDKs updated

## Future Enhancements

1. **Async/Await Support**: For better performance
2. **Caching Layer**: Redis or file-based cache
3. **Database Integration**: Store generated syllabi
4. **Web API**: FastAPI endpoints
5. **Frontend**: React-based UI
6. **Batch Processing**: Generate multiple syllabi
7. **Template System**: Pre-defined course templates
8. **Content Generation**: Generate full lesson content
9. **Assessment Creation**: Quizzes and exercises
10. **Export Formats**: PDF, SCORM, HTML
