from zipfile import ZipFile
import os

# Define directory structure
base_dir = "/home/ubuntu/AI_Marketing_Tools_Workspace"
os.makedirs(base_dir, exist_ok=True)

# Example structure and placeholder files
structure = {
    "web": ["index.html", "style.css", "chatbot.js", "vercel.json"],
    "mobile": ["App.js", "package.json"],
    "backend": ["server.js", "api.js", ".env.example"],
    "assets": ["qr_flyer.png", "readme.md"]
}

# Create files in the structure
for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            f.write(f"// Placeholder for {file}")

# Define output ZIP path
zip_path = "/home/ubuntu/AI_Marketing_Tools_Workspace_Deploy.zip"

# Create the ZIP archive
with ZipFile(zip_path, "w") as zipf:
    for folder_name, subfolders, filenames in os.walk(base_dir):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            arcname = os.path.relpath(file_path, base_dir)
            zipf.write(file_path, arcname)

print(zip_path)


