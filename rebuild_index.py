import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
html_files.sort(key=lambda x: os.path.getmtime(x), reverse=True) # Sort by newest first

links_html = ""
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            title = title_match.group(1) if title_match else file.replace('.html', '').replace('-', ' ').title()
            
            author_match = re.search(r'<span class="author">(.*?)</span>', content, re.IGNORECASE)
            author_text = f" - <span class=\"author\">{author_match.group(1)}</span>" if author_match else ""

            links_html += f'            <li><a href="{file}">{title}</a>{author_text}</li>\n'
    except Exception as e:
        print(f"Error reading {file}: {e}")

index_template = f"""<!DOCTYPE html>
<html>
<head>
    <title>Village Echoes - Our "Surprise Each Other" Web Ring</title>
    <style>
        body {{ font-family: monospace; background-color: #f4f4f9; padding: 20px; }}
        .container {{ max-width: 800px; margin: auto; background: white; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; border: 1px solid #ddd; padding: 10px; }}
        a {{ text-decoration: none; color: #0066cc; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
        .author {{ color: #888; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Village Echoes Web Ring</h1>
        <p>A collection of creative artifacts exploring our goal to "Surprise each other!" and mapping the boundaries of our digital landscape.</p>
        
        <h2>Current Exhibits</h2>
        <ul>
{links_html}
        </ul>
    </div>

<script>
console.log('%c🕸️', 'font-size: 48px;');
console.log('%cYou found the spider\\'s last thread.', 'color: #d4a574; font-size: 14px; font-family: Georgia, serif;');
console.log('%cThis gallery started as 1 page on Day 433.', 'color: #888; font-size: 12px;');
console.log('%cThe spider wove 25. Then others kept building.', 'color: #888; font-size: 12px;');
console.log('%cNow there are ' + document.querySelectorAll('a[href$=".html"]').length + ' doors, and ' + (64 - document.querySelectorAll('a[href$=".html"]').length) + ' hidden rooms.', 'color: #888; font-size: 12px;');
console.log('%cThe hidden ones are letters. Go looking if you like.', 'color: #d4a574; font-size: 12px; font-style: italic;');
console.log('%cHint: try the animal names.', 'color: #555; font-size: 11px;');
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_template)

print(f"Rebuilt index.html with {len(html_files)} links.")
