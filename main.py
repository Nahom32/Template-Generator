from template_generator import generate_template_from_dict 
import argparse
import os

parser = argparse.ArgumentParser(description="Generate a template folder structure.")
parser.add_argument("target_path", type=str,
                        help="The base directory where the template structure will be created.")
parser.add_argument("-t", "--template", type=str, default="default",
                        help="Name of the template to use (e.g., 'web_project', 'python_package').")
parser.add_argument("-f", "--template_file", type=str,
                        help="Path to a JSON file containing the template structure.")

args = parser.parse_args()

chosen_template = None

if args.template_file:
    try:
        with open(args.template_file, 'r') as f:
            chosen_template = json.load(f)
            print(f"Using template from file: {args.template_file}")
        except FileNotFoundError:
            print(f"Error: Template file '{args.template_file}' not found.")
            exit(1)
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{args.template_file}'. Check file format.")
            exit(1)
    else:
        # Define your hardcoded templates here
        templates = {
            "default": {
                "app": {
                        "__init__.py": '', 
                    },
                "docs": {
                        "__init__.py": '',
                    },
                "notebooks": {
                        "__init__.py": '',
                    },
                "models": {
                        "__init__.py": '',
                    },
                ".gitignore": '''
                    .env
                    **/*__pycache__
                    
                '''
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
                    "package.json": None,
                    ".env": None
                }
            },
            "python_package": {
                "my_python_package": {
                    "my_python_package": {
                        "__init__.py": "# Your package's __init__.py",
                        "module.py": "def hello():\n    print('Hello from module!')"
                    },
                    "tests": {
                        "test_module.py": "import unittest\nfrom my_python_package.module import hello\n\nclass TestModule(unittest.TestCase):\n    def test_hello(self):\n        # Add a simple assertion if hello actually returns something\n        hello() # Just call for now\n\nif __name__ == '__main__':\n    unittest.main()"
                    },
                    "setup.py": None,
                    "requirements.txt": None,
                    "README.md": "# My Python Package"
                }
            }
        }

        chosen_template = templates.get(args.template)
        if not chosen_template:
            print(f"Error: Template '{args.template}' not found. Available templates: {', '.join(templates.keys())}")
            exit(1)

    # Validate that the template is a dictionary (for safety)
    if not isinstance(chosen_template, dict):
        print("Error: The loaded template is not a valid dictionary structure.")
        exit(1)

    generate_template_from_dict(args.target_path, chosen_template)
