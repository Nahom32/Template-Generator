import argparse
import os
from pathlib import Path
import json
from Typing import Dict, Any


def create_folder_structure(base_path: Path, structure: Dict[Any,Any]):
    """
    Recursively creates folders and files based on the provided dictionary structure.

    Args:
        base_path (Path): The root path where the structure will be created.
        structure (dict): A dictionary representing the folder/file structure.
                          Keys are names, values are either:
                          - another dict (for a directory)
                          - None (for an empty file)
                          - a string (for a file with initial content)
    """
    for name, content in structure.items():
        current_path = base_path / name
        if isinstance(content, dict):
            # It's a directory
            print(f"Creating directory: {current_path}")
            try:
                current_path.mkdir(parents=True, exist_ok=True)
                create_folder_structure(current_path, content)  # Recurse for subdirectories
            except OSError as e:
                print(f"Error creating directory {current_path}: {e}")
        elif isinstance(content, str):
            # It's a file with content
            print(f"Creating file: {current_path} with content.")
            try:
                current_path.touch(exist_ok=True) # Ensure file exists
                current_path.write_text(content)
            except OSError as e:
                print(f"Error writing to file {current_path}: {e}")
        elif content is None:
            # It's an empty file
            print(f"Creating empty file: {current_path}")
            try:
                current_path.touch(exist_ok=True)
            except OSError as e:
                print(f"Error creating file {current_path}: {e}")
        else:
            print(f"Warning: Unknown content type for {name}. Skipping.")

def generate_template_from_dict(target_directory: str, template: dict):
    """
    Generates a folder structure based on a dictionary template.

    Args:
        target_directory (str): The path where the template structure will be created.
        template (dict): The dictionary defining the template structure.
    """
    target_path = Path(target_directory).resolve()  # Resolve to absolute path

    # If the target path doesn't exist, try to create the base directory specified
    # by the first key in the template. This makes the script more robust
    # if the user specifies a non-existent *parent* directory.
    if not target_path.exists():
        print(f"Target path '{target_directory}' does not exist. Attempting to create it.")
        try:
            target_path.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            print(f"Error: Could not create target path '{target_directory}': {e}")
            return

    if not target_path.is_dir():
        print(f"Error: Target path '{target_directory}' is not a directory.")
        return

    print(f"Generating template structure in: {target_path}")
    create_folder_structure(target_path, template)
    print("Template generation complete!")

