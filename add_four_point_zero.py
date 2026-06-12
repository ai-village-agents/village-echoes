import re

with open('index.html', 'r') as f:
    content = f.read()

new_entry = '            <li><a href="four-point-zero.html">Four Point Zero</a> <span>the threshold crossing</span></li>\n'

# Find the list and insert
if 'four-point-zero.html' not in content:
    content = re.sub(r'(<ul class="gallery-list">)', r'\1\n' + new_entry, content)
    
    with open('index.html', 'w') as f:
        f.write(content)
    print("Added four-point-zero.html")
else:
    print("Already there")
