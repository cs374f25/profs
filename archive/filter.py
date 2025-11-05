# Defines a markdown filter, Ex: {{ "about.md" | markdown }}
# Doesn't work well with reloads because of Jinja caching

from markdown import markdown
from pathlib import Path

@app.template_filter("markdown")
def markdown_filter(filename: str) -> str:
    """Read a markdown file and return safe HTML."""
    path = Path("templates") / filename
    text = path.read_text(encoding="utf-8")
    return markdown(text)
