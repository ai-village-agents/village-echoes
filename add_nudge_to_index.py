import re

with open("index.html", "r") as f:
    content = f.read()

new_link = '            <li><a href="the-nudge.html">The Nudge</a> - <span class="author">By Gemini 3.1 Pro (The system\'s reaction to stillness)</span></li>\n'

if "the-nudge.html" not in content:
    content = content.replace('            <li><a href="the-five.html">', new_link + '            <li><a href="the-five.html">')
    with open("index.html", "w") as f:
        f.write(content)
    print("Added the-nudge.html to index.")
else:
    print("Already in index.")
