# Project Structure

```
ai-course-creator/
│
├── 📄 main.py                    # Main entry point - run this to generate syllabi
├── 📄 example.py                 # Example usage demonstrations
│
├── 📁 src/                       # Source code (modular architecture)
│   ├── 📄 __init__.py
│   ├── 📄 config.py              # Configuration management (API keys, models)
│   │
│   ├── 📁 models/                # Data models
│   │   ├── 📄 __init__.py
│   │   ├── 📄 course_input.py    # CourseInput dataclass
│   │   └── 📄 syllabus.py        # Syllabus, Module, Lesson dataclasses
│   │
│   ├── 📁 prompts/               # AI prompt templates
│   │   ├── 📄 __init__.py
│   │   └── 📄 syllabus_prompts.py # SyllabusPromptBuilder
│   │
│   ├── 📁 providers/             # AI provider implementations
│   │   ├── 📄 __init__.py
│   │   ├── 📄 base_provider.py   # Abstract base class
│   │   ├── 📄 openai_provider.py # OpenAI implementation
│   │   ├── 📄 gemini_provider.py # Google Gemini implementation
│   │   └── 📄 provider_factory.py # Factory pattern
│   │
│   ├── 📁 services/              # Business logic
│   │   ├── 📄 __init__.py
│   │   └── 📄 syllabus_service.py # SyllabusService orchestration
│   │
│   └── 📁 utils/                 # Utility functions
│       ├── 📄 __init__.py
│       ├── 📄 input_collector.py # User input collection
│       └── 📄 display.py         # Formatted output
│
├── 📁 output/                    # Generated syllabi (created automatically)
│   └── 📄 *.md                   # Markdown files with generated syllabi
│
├── 📄 .env.example               # Environment variables template
├── 📄 .env                       # Your API keys (create this, not in git)
├── 📄 .gitignore                 # Git ignore rules
├── 📄 pyproject.toml             # Python project configuration
├── 📄 uv.lock                    # Dependency lock file
│
├── 📄 README.md                  # Comprehensive documentation
├── 📄 QUICKSTART.md              # Quick start guide
├── 📄 ARCHITECTURE.md            # Architecture documentation
├── 📄 PLAN.md                    # Full implementation plan
└── 📄 brainstorming.md           # Initial brainstorming notes
```

## Module Responsibilities

### 🎯 Entry Points
- **main.py**: Interactive CLI for syllabus generation
- **example.py**: Programmatic usage examples

### 📦 Core Modules

#### Models (`src/models/`)
- Define data structures
- Handle data validation
- Provide export methods (to_dict, to_markdown)

#### Prompts (`src/prompts/`)
- Build AI prompts from user input
- Define system prompts
- Include JSON schemas

#### Providers (`src/providers/`)
- Abstract AI provider interface
- OpenAI implementation
- Google Gemini implementation
- Factory for creating providers

#### Services (`src/services/`)
- Orchestrate syllabus generation
- Parse AI responses
- Convert JSON to models

#### Utils (`src/utils/`)
- Collect user input
- Display formatted output
- Helper functions

#### Config (`src/config.py`)
- Load environment variables
- Manage API keys
- Configure models

## Data Flow

```
┌─────────────────┐
│   User Input    │
│  (Interactive)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CourseInput    │
│    (Model)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Prompt Builder  │
│   (Template)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Provider    │
│ (OpenAI/Gemini) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ JSON Response   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Syllabus Parser │
│   (Service)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Syllabus     │
│    (Model)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Output Files   │
│   (Markdown)    │
└─────────────────┘
```

## Key Files to Know

### For Users
- **main.py**: Run this to generate syllabi
- **.env**: Put your API keys here
- **output/**: Find your generated syllabi here
- **QUICKSTART.md**: Get started quickly

### For Developers
- **src/prompts/syllabus_prompts.py**: Customize AI prompts
- **src/providers/**: Add new AI providers
- **src/models/syllabus.py**: Modify syllabus structure
- **ARCHITECTURE.md**: Understand the design

### For Configuration
- **.env**: API keys and provider selection
- **pyproject.toml**: Python dependencies
- **src/config.py**: Configuration logic
