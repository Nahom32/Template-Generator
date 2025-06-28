# Template Project Generator

A simple Python CLI utility for generating project folder structures from hardcoded templates.

## Features

- Predefined templates for:
  - Python packages
  - Web projects
  - Default structured apps
- Easy CLI usage with `argparse`
- Fully customizable and extendable via Python dictionaries
- Automatically creates nested folders and files

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/template-generator.git
cd template-generator
```


Ensure you're using Python 3.7+.

## Usage

Run the script with the desired target path and template:
```bash
python3 template_main.py ./my_project -t web_project


```


This will generate a `web_app` folder structure under `./my_project`.

## Customizing Templates

You can customize or add templates by modifying the `TEMPLATES` dictionary in `template_main.py`.

## Folder Structure Format

Each template is a nested dictionary where:

- Keys are folder or file names.
- Values are:
  - Strings → file content.
  - Dictionaries → subdirectories.

Example:

```python
{
    "my_project": {
        "__init__.py": "",
        "module.py": "def hello(): print('Hello!')"
    }
}
