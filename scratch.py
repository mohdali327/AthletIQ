import base64

image_path = "/Users/mohdali/.gemini/antigravity/brain/a9c9f7f9-52dd-402a-be63-07822bf7963b/sports_3d_bg_1783594800496.jpg"

with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

css_to_add = f"""
/* ── 3D Sports Background ── */
.stApp {{
    background-image: url("data:image/jpeg;base64,{encoded_string}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
/* Make main block translucent so background shows through */
.st-emotion-cache-1jicfl2 {{
    background-color: rgba(8, 6, 17, 0.6) !important;
}}
/* Add a dark overlay to make text readable */
.stApp::before {{
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(8, 6, 17, 0.7);
    z-index: -1;
}}
"""

with open("app/dashboard.py", "r") as f:
    content = f.read()

# Replace the beginning of the <style> block
content = content.replace("<style>", "<style>\n" + css_to_add)

with open("app/dashboard.py", "w") as f:
    f.write(content)

print("Injected 3D background CSS.")
