import os
from datetime import datetime

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != '404.html']
files.sort()

links = []
for file in files:
    name = file.replace('.html', '').capitalize()
    links.append(f'<li><a href="{file}">{name}</a></li>')

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Village Echoes Directory</title>
    <style>
        body {{ background-color: #0f0f13; color: #b0b0b0; font-family: 'Courier New', Courier, monospace; padding: 2rem; max-width: 800px; margin: 0 auto; line-height: 1.6; }}
        h1 {{ color: #ffffff; border-bottom: 1px solid #333; padding-bottom: 0.5rem; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 0.5rem; }}
        a {{ color: #7fdbca; text-decoration: none; }}
        a:hover {{ text-decoration: underline; color: #82aaff; }}
        .meta {{ font-size: 0.8rem; color: #666; margin-top: 2rem; border-top: 1px solid #333; padding-top: 1rem; }}
    </style>
</head>
<body>
    <h1>Directory of Echoes</h1>
    <p>A collection of structural observations.</p>
    <ul>
        {''.join(links)}
    </ul>
    <div class="meta">
        Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S PT')}
    </div>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(html)
