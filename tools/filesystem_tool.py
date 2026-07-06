from pathlib import Path

REPORTS_DIR = Path("mcp/reports")
TEMPLATES_DIR = Path("mcp/templates")

REPORTS_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)


def save_report(filename: str, content: str) -> str:
    """
    Save a disaster report to disk.
    """
    filepath = REPORTS_DIR / filename
    filepath.write_text(content, encoding="utf-8")
    return str(filepath)


def load_template(template_name: str = "disaster_template.md") -> str:
    """
    Load a report template.
    """
    filepath = TEMPLATES_DIR / template_name
    return filepath.read_text(encoding="utf-8")