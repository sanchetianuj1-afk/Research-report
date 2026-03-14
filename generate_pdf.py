#!/usr/bin/env python3
"""Convert the Tata Steel Equity Research Report from Markdown to a one-page PDF."""

import markdown
from weasyprint import HTML

MD_FILE = "Tata_Steel_Equity_Research_Report.md"
PDF_FILE = "Tata_Steel_Equity_Research_Report.pdf"

CSS = """
@page {
    size: A4;
    margin: 1.5cm 1.8cm;
}
body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 9pt;
    line-height: 1.35;
    color: #1a1a1a;
}
h1 {
    font-size: 14pt;
    margin: 0 0 2pt 0;
    color: #003366;
    border-bottom: 2px solid #003366;
    padding-bottom: 3pt;
}
h2 {
    font-size: 10pt;
    margin: 6pt 0 2pt 0;
    color: #003366;
}
p {
    margin: 2pt 0;
}
ul {
    margin: 2pt 0 2pt 14pt;
    padding: 0;
}
li {
    margin-bottom: 1pt;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 4pt 0;
    font-size: 8.5pt;
}
th, td {
    border: 1px solid #999;
    padding: 2pt 5pt;
    text-align: right;
}
th {
    background-color: #003366;
    color: #fff;
    font-weight: bold;
}
td:first-child, th:first-child {
    text-align: left;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 4pt 0;
}
strong {
    color: #003366;
}
em {
    font-size: 8pt;
    color: #555;
}
a {
    color: #003366;
}
"""

with open(MD_FILE, "r") as f:
    md_text = f.read()

html_body = markdown.markdown(md_text, extensions=["tables"])

full_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{CSS}</style></head>
<body>{html_body}</body>
</html>"""

HTML(string=full_html).write_pdf(PDF_FILE)
print(f"PDF generated: {PDF_FILE}")
