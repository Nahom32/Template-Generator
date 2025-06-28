#!/bin/bash

# Define the absolute path to your Python script
# It's best practice to put your scripts in a central location, e.g., ~/.local/bin/
# For demonstration, let's assume it's in a 'scripts' directory in your home folder.
PYTHON_SCRIPT_PATH="$HOME/scripts/generate_template.py"

# --- Check if the Python script exists ---
if [ ! -f "$PYTHON_SCRIPT_PATH" ]; then
    echo "Error: Python script not found at $PYTHON_SCRIPT_PATH."
    echo "Please ensure 'generate_template.py' is in the specified location."
    exit 1
fi

# --- Check for Python interpreter ---
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 could not be found."
    echo "Please ensure Python 3 is installed and available in your PATH."
    exit 1
fi

# --- Execute the Python script with all arguments ---
# $1, $2, etc., capture positional arguments
# $@ passes all arguments (including options like -t, -f) directly to the python script
python3 "$PYTHON_SCRIPT_PATH" "$@"
