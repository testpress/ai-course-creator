# Quick Start Guide

Get up and running with the AI Course Creator in 5 minutes!

## Prerequisites

- Python 3.12 or higher
- An API key from either:
  - [OpenAI](https://platform.openai.com/api-keys) (recommended for beginners)
  - [Google AI Studio](https://makersuite.google.com/app/apikey) (for Gemini)

## Installation Steps

### 1. Install Dependencies

Using `uv` (recommended):
```bash
uv sync
```

Or using `pip`:
```bash
pip install -e .
```

### 2. Set Up Your API Key

**Option A: Using Environment File (Recommended)**

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your API key:
   ```env
   # For OpenAI
   AI_PROVIDER=openai
   OPENAI_API_KEY=sk-your-actual-api-key-here
   OPENAI_MODEL=gpt-4o-mini
   ```
   
   OR
   
   ```env
   # For Google Gemini
   AI_PROVIDER=gemini
   GEMINI_API_KEY=your-actual-api-key-here
   GEMINI_MODEL=gemini-1.5-flash
   ```

**Option B: Interactive Setup**

If you skip the `.env` file, the program will prompt you for your API key when you run it.

### 3. Run the Generator

```bash
python main.py
```

## Example Usage

Here's what a typical session looks like:

```
============================================================
AI Course Creator - Syllabus Generator
============================================================

Enter the course topic/subject: Introduction to Machine Learning

Complexity Level (optional - press Enter to skip):
1. Beginner
2. Intermediate
3. Advanced
Select complexity (1-3 or Enter to skip): 1

Age group (optional - press Enter to skip): College students

Tone/Style (optional - press Enter to skip):
1. Academic
2. Casual
3. Professional
4. Humorous
Select tone (1-4 or Enter to skip): 3

============================================================
Collected Information:
============================================================
Topic/Subject: Introduction to Machine Learning
Complexity: Beginner
Age Group: College students
Tone/Style: Professional
============================================================

[INFO] Setting up AI provider...
[INFO] Using OPENAI with model gpt-4o-mini
[INFO] Validating API key...
[INFO] Generating syllabus... This may take a moment.

============================================================
Generated Syllabus
============================================================

# Introduction to Machine Learning

## Course Description
[Generated course description...]

## Course Modules

### Module 1: Foundations of Machine Learning
...

============================================================

✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓
Syllabus saved to: output/introduction_to_machine_learning_syllabus.md
✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓
```

## Output

The generated syllabus will be:
1. **Displayed** in your terminal
2. **Saved** as a Markdown file in the `output/` directory
3. **Stored** in a variable for programmatic access

## Programmatic Usage

You can also use the system programmatically:

```python
from src.config import Config
from src.models.course_input import CourseInput
from src.providers import ProviderFactory
from src.services import SyllabusService

# Setup
config = Config.from_env()
provider = ProviderFactory.create_provider(
    provider_name=config.ai_provider,
    api_key=config.get_api_key()
)
service = SyllabusService(ai_provider=provider)

# Generate
course_input = CourseInput(
    topic="Python Programming",
    complexity="Beginner"
)
syllabus = service.generate_syllabus(course_input)

# Use the syllabus
print(syllabus.course_title)
print(syllabus.to_markdown())
```

See `example.py` for more examples.

## Troubleshooting

### "No API key found"
- Make sure you've created a `.env` file
- Check that your API key is correctly set in the `.env` file
- Verify there are no extra spaces or quotes around the key

### "Invalid API key"
- Verify your API key is active on the provider's website
- Check that you're using the correct provider (OpenAI vs Gemini)
- Make sure you have credits/quota available

### "Import errors"
- Run `uv sync` or `pip install -e .` again
- Make sure you're using Python 3.12 or higher

### "JSON parsing error"
- This is rare, but try running again
- Try switching to a different model (e.g., gpt-4o instead of gpt-4o-mini)

## Next Steps

1. **Explore the output**: Check the `output/` directory for your generated syllabi
2. **Try different topics**: Generate syllabi for various subjects
3. **Customize prompts**: Edit `src/prompts/syllabus_prompts.py` to adjust the generation
4. **Read the docs**: Check `ARCHITECTURE.md` for detailed system documentation
5. **Extend the system**: Add new features or AI providers

## Cost Considerations

### OpenAI (gpt-4o-mini)
- Very affordable: ~$0.15 per million input tokens
- A typical syllabus generation costs less than $0.01

### Google Gemini (gemini-1.5-flash)
- Free tier: 15 requests per minute
- Very generous free quota
- Great for development and testing

## Tips for Best Results

1. **Be specific**: "Python for Data Science" is better than just "Python"
2. **Set complexity**: Helps the AI adjust the depth of content
3. **Specify audience**: "High school students" vs "Professionals" makes a difference
4. **Choose appropriate tone**: Academic for formal courses, Casual for general learning

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review `README.md` for detailed documentation
3. Check `ARCHITECTURE.md` for system design details
4. Review the code in `src/` - it's well-documented!

Happy course creating! 🎓
