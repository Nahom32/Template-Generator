from template_generator import generate_template_from_dict 
import argparse
import os
import json

# Define available hardcoded templates
TEMPLATES = {
    "default": {
        "app": {"__init__.py": ""},
        "docs": {"__init__.py": ""},
        "notebooks": {"__init__.py": ""},
        "models": {"__init__.py": ""},
        "datasets": {"__init__.py": ""},
        ".gitignore": ".env\n**/*__pycache__\n",
        "Dockerfile": ""
    },
    "web_project": {
        "web_app": {
            "public": {
                "index.html": "<!DOCTYPE html>\n<html><head><title>Web App</title></head><body><h1>Welcome!</h1></body></html>",
                "css": {},
                "js": {}
            },
            "src": {
                "components": {},
                "pages": {}
            },
            "node_modules": {},
            "package.json": "",
            ".env": ""
        }
    },
    "python_package": {
        "my_python_package": {
            "my_python_package": {
                "__init__.py": "# Your package's __init__.py",
                "module.py": "def hello():\n    print('Hello from module!')"
            },
            "tests": {
                "test_module.py": (
                    "import unittest\n"
                    "from my_python_package.module import hello\n\n"
                    "class TestModule(unittest.TestCase):\n"
                    "    def test_hello(self):\n"
                    "        hello()\n\n"
                    "if __name__ == '__main__':\n"
                    "    unittest.main()"
                )
            },
            "setup.py": "",
            "requirements.txt": "",
            "README.md": "# My Python Package"
        }
    }
}

def main():
    parser = argparse.ArgumentParser(description="Generate a template folder structure.")
    parser.add_argument("target_path", type=str, help="Base directory where the template will be created.")
    parser.add_argument("-t", "--template", type=str, default="default",
                        help=f"Template to use (options: {', '.join(TEMPLATES.keys())})")

    args = parser.parse_args()
    selected_template = TEMPLATES.get(args.template)

    if not selected_template:
        print(f"Error: Template '{args.template}' not found.")
        print(f"Available templates: {', '.join(TEMPLATES.keys())}")
        exit(1)

    if not os.path.isdir(args.target_path):
        try:
            os.makedirs(args.target_path)
            print(f"Created target directory: {args.target_path}")
        except Exception as e:
            print(f"Error: Could not create target directory. {e}")
            exit(1)

    print(f"Using template: {args.template}")
    generate_template_from_dict(args.target_path, selected_template)

if __name__ == "__main__":
    main()
