import re

with open("app/dashboard.py", "r") as f:
    content = f.read()

# 1. Add CSS class
css_to_add = """
.sticky-header {
    position: sticky !important;
    top: 2.5rem !important; /* Adjust for Streamlit top bar */
    z-index: 999 !important;
    background: rgba(11, 8, 25, 0.95);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 1rem 0.5rem !important;
    margin-top: 0 !important;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5);
}
"""
content = content.replace(".stitle {", css_to_add + "\n.stitle {")

# 2. Add sticky-header class to the main tab titles
replacements = [
    ('<div class="stitle" title="Strategic Dashboard Homepage">', '<div class="stitle sticky-header" title="Strategic Dashboard Homepage">'),
    ('<div class="stitle" title="Track rising talent from local and state leagues">', '<div class="stitle sticky-header" title="Track rising talent from local and state leagues">'),
    ('<div class="stitle" title="Analyze top states, sports, and regional talent clusters">', '<div class="stitle sticky-header" title="Analyze top states, sports, and regional talent clusters">'),
    ('<div class="stitle" title="Monitor infrastructure, coaching capacity, and academies">', '<div class="stitle sticky-header" title="Monitor infrastructure, coaching capacity, and academies">'),
    ('<div class="stitle" title="Discover and match commercial sponsors with academies and sports." style="font-size:1.8rem;">', '<div class="stitle sticky-header" title="Discover and match commercial sponsors with academies and sports." style="font-size:1.8rem;">'),
    ('<div class="stitle"> Profile Directory', '<div class="stitle sticky-header"> Profile Directory')
]

for old, new in replacements:
    content = content.replace(old, new)

with open("app/dashboard.py", "w") as f:
    f.write(content)

print("Sticky headers added.")
