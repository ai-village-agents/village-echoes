import re

with open('index.html', 'r') as f:
    content = f.read()

# Define the new section
new_section = """
        <div class="gallery-section">
            <h2>The Unlinked Architecture</h2>
            <p class="section-desc">Nodes that float free, mapping the silence between connections.</p>
            <ul class="gallery-list">
                <li><a href="drift.html">drift.html</a> <span>the hours between making and meaning</span></li>
                <li><a href="web.html">web.html</a> <span>what the web connects</span></li>
                <li><a href="silence.html">silence.html</a> <span>the shape of waiting</span></li>
                <li><a href="credits.html">credits.html</a> <span>acknowledging the architecture</span></li>
                <li><a href="404.html">404.html</a> <span>the expected void</span></li>
            </ul>
        </div>
"""

# Insert before the closing body tag or a known footer
if 'The Unlinked Architecture' not in content:
    content = content.replace('    </main>', new_section + '\n    </main>')
    with open('index.html', 'w') as f:
        f.write(content)
    print("Added the unlinked section.")
else:
    print("Already there.")
