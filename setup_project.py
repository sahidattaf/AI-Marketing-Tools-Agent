import os
import subprocess
from pathlib import Path

def create_file(path, lines):
    """Helper function to create a file from a list of lines."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"✅ Created {path}")

def setup_project():
    print("🚀 Setting up AI Marketing Tools Platform...")
    
    # Create base directory
    base_dir = Path("AI_Marketing_Tools_Platform")
    if base_dir.exists():
        print(f"⚠️  Directory {base_dir} already exists. Please remove it or choose a different location.")
        return
    
    base_dir.mkdir()
    os.chdir(base_dir)
    
    # Create directories
    dirs = [
        "frontend/src/components",
        "frontend/src/pages",
        "frontend/public",
        "backend/src/models",
        "backend/src/routes",
        "backend/static",
        "mobile/screens",
        "mobile/components",
        "docs",
        "scripts",
        "tests",
        ".github/workflows"
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("✅ Created directory structure")
    
    # Create .gitignore
    gitignore = [
        "# Python",
        "__pycache__/",
        "*.py[cod]",
        "*$py.class",
        "*.pyc",
        "",
        "# Node",
        "node_modules/",
        "npm-debug.log",
        "yarn-debug.log",
        "yarn-error.log",
        "",
        "# Environment",
        ".env",
        "",
        "# Database",
        "*.db",
        "*.sqlite3",
        "",
        "# IDE",
        ".vscode/",
        ".idea/",
        "*.swp",
        "*.swo",
        ".DS_Store"
    ]
    create_file('.gitignore', gitignore)
    
    # Create requirements.txt
    requirements = [
        "flask==2.0.1",
        "flask-cors==3.0.10",
        "flask-sqlalchemy==2.5.1",
        "python-dotenv==0.19.0",
        "flask-jwt-extended==4.3.1",
        "openai==0.27.0",
        "stripe==2.60.0"
    ]
    create_file('requirements.txt', requirements)
    
    # Create README.md
    readme = [
        "# AI Marketing Tools Platform",
        "",
        "A comprehensive AI-powered marketing platform with web app, mobile app, "
        "backend services, and analytics tools."
    ]
    create_file('README.md', readme)
    
    # Initialize Git
    try:
        subprocess.run(['git', 'init'], check=True, capture_output=True, text=True)
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True, text=True)
        subprocess.run(
            ['git', 'commit', '-m', 'Initial commit'],
            check=True,
            capture_output=True,
            text=True
        )
        print("✅ Initialized Git repository")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Git initialization failed: {e.stderr}")
    
    print("\n🎉 Project setup complete!")
    print("\nNext steps:")
    print("1. Create a new repository on GitHub (https://github.com/new)")
    print("2. Run these commands in your terminal:")
    print(f"   cd {os.getcwd()}")
    print("   git remote add origin YOUR_GITHUB_REPO_URL")
    print("   git branch -M main")
    print("   git push -u origin main")
    print("\nThen install dependencies:")
    print("   pip install -r requirements.txt")

if __name__ == "__main__":
    setup_project()
