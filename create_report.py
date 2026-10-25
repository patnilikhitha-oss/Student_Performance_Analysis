
from pathlib import Path
import markdown

# Project folder
project_dir = Path(__file__).parent

# Input Markdown report
markdown_file = project_dir / "project_report.md"

# Output HTML report
html_file = project_dir / "project_report.html"

# Read the Markdown report
if not markdown_file.exists():
    print("ERROR: project_report.md was not found.")
    raise SystemExit(1)

report_text = markdown_file.read_text(encoding="utf-8")

# Convert Markdown to HTML and support embedded images
html_body = markdown.markdown(
    report_text,
    extensions=["tables", "fenced_code"]
)

# Add simple, readable styling
html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Performance Analysis</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 35px auto;
            padding: 0 22px;
            line-height: 1.7;
            color: #222;
            background: #fff;
        }}
        h1, h2, h3 {{
            color: #17365D;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 18px 0;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background: #eaf1f8;
        }}
        img {{
            display: block;
            max-width: 100%;
            height: auto;
            margin: 18px auto;
        }}
        code {{
            background: #f2f2f2;
            padding: 2px 5px;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

# Save HTML report
html_file.write_text(html_page, encoding="utf-8")

print("SUCCESS: HTML report created.")
print(f"Report location: {html_file}")
print("Check that all three graph images appear in the report.")
