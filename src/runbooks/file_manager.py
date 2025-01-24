#!/usr/bin/env python3

"""
Utilities to create a specified folder and an empty file inside it with safe error handling.

Author: Python Developer
Date: 2025-01-05
Version: 1.0.0

Usage:
    file_manager.py <folder_name> <file_name>
"""

import os
import sys
from pathlib import Path
from typing import Union


## ==============================
## VALIDATION UTILITIES
## ==============================
def validate_input(value: Union[str, float, int]) -> float:
    """
    Validates and converts input into a float.

    Args:
        value (Union[str, float, int]): The input value to validate and convert.

    Returns:
        float: The validated and converted float value.

    Raises:
        TypeError: If input type is unsupported.
        ValueError: If input cannot be converted to float, or fails constraints.
    """

    ## ✅ Step 1.1: Input Type Validation
    if not isinstance(value, (str, int, float)):
        raise TypeError(f"Invalid type '{type(value).__name__}'. Expected str, int, or float.")

    ## ✅ Step 1.2: Handle Empty String
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"Invalid input '{value}'. Input cannot be empty or whitespace-only.")

    ## ✅ Step 2: Convert Input to Float
    try:
        result = float(value) ## Attempt numeric conversion
    except ValueError as e:
        raise ValueError(f"Invalid input '{value}'. Must be a valid number.") from e

    ## ✅ Step 3: Return Validated Float
    return result


def validate_folder_name(folder_name: str) -> None:
    """
    Validates folder name for OS-specific constraints.

    Args:
        folder_name (str): The folder name to validate.

    Raises:
        ValueError: If the folder name violates naming constraints.
    """
    if not folder_name:
        raise ValueError("Folder name cannot be empty.")

    if len(folder_name) > 255:  # Max length in most file systems
        raise ValueError("Folder name exceeds maximum length (255 characters).")

    invalid_chars = '<>:"/\\|?*'  # Reserved characters in Windows
    if any(char in invalid_chars for char in folder_name):
        raise ValueError(f"Folder name '{folder_name}' contains invalid characters.")

    if folder_name in {"CON", "PRN", "AUX", "NUL"}:  # Reserved Windows names
        raise ValueError(f"Folder name '{folder_name}' is a reserved keyword.")

    if folder_name.startswith(' ') or folder_name.endswith(' '):
        raise ValueError("Folder name cannot start or end with spaces.")


def validate_file_name(file_name: str) -> None:
    """
    Validates file name for OS-specific constraints.

    Args:
        file_name (str): The file name to validate.

    Raises:
        ValueError: If the file name violates naming constraints.
    """
    if not file_name:
        raise ValueError("File name cannot be empty.")

    if len(file_name) > 255:
        raise ValueError("File name exceeds maximum length (255 characters).")

    invalid_chars = '<>:"/\\|?*'
    if any(char in invalid_chars for char in file_name):
        raise ValueError(f"File name '{file_name}' contains invalid characters.")

    if file_name.startswith(' ') or file_name.endswith(' '):
        raise ValueError("File name cannot start or end with spaces.")

    if len(Path(file_name).suffix) == 0:  # Ensure file has an extension
        raise ValueError("File name must include a valid extension (e.g., '.txt').")


## ==============================
## FILE SYSTEM UTILITIES
## ==============================
def create_folder_and_file(folder_name: str, file_name: str) -> None:
    """
    Create a folder and an empty file safely with robust error handling.

    Args:
        folder_name (str): Name of the folder to be created.
        file_name (str): Name of the file to be created inside the folder.

    Raises:
        FileExistsError: If the folder already exists.
        FileNotFoundError: If the folder path is invalid.
        PermissionError: If there are insufficient permissions.
        ValueError: If inputs are invalid.
    """
    ## ✅ Input Validation
    validate_folder_name(folder_name)
    validate_file_name(file_name)

    ## ✅ Create Path Object
    folder_path = Path(folder_name)
    file_path = folder_path / file_name

    try:
        ## ✅ Create folder if it doesn't exist; same behavior as the POSIX `mkdir -p` command
        folder_path.mkdir(parents=True, exist_ok=True) ## Safe parent directory creation
        print(f"✅ Folder '{folder_name}' created successfully.")

        ## ✅ Create an empty file inside the folder
        # os.chdir(folder_name) ## May Raise FileNotFoundError
        # with open(file_name, 'a'):
        #     pass
        if file_path.exists():
            raise FileExistsError(f"File '{file_name}' already exists in '{folder_name}'.")

        file_path.touch(exist_ok=False)  ## Create an empty file; Fails safely if file exists
        print(f"✅ File '{file_name}' created successfully inside '{folder_name}'.")

    except FileExistsError as e:
        raise FileExistsError(str(e))  # Re-raise exception without exiting

    except PermissionError:
        print("❌ Permission denied. Check your user permissions.")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

## ✅ Handle Arguments Dynamically for Terminal and Debugger Compatibility
def parse_arguments() -> tuple[str, str]:
    """
    Parses and validates command-line arguments for both terminal and VSCode debugger compatibility.

    Returns:
        tuple[str, str]: A tuple containing folder_name and file_name.

    Raises:
        ValueError: If arguments are invalid or insufficient.
    """
    import shlex  # Safely split arguments with quotes (if present)

    ## ✅ Check Arguments Length
    if len(sys.argv) < 2:
        raise ValueError("Provide exactly 2 arguments: <folder_name> <file_name>")

    ## ✅ Handle Debugger Inputs (Single Combined Argument)
    if len(sys.argv) == 2:
        args = shlex.split(sys.argv[1])  # Split safely with quote handling
    else:
        args = sys.argv[1:]  # Use normal command-line arguments

    ## ✅ Validate Number of Arguments
    if len(args) != 2:
        raise ValueError("❌ Invalid arguments. Provide exactly 2 arguments: <folder_name> <file_name>")

    ## ✅ Extract Folder and File Names
    folder_name, file_name = args[0], args[1]
    return folder_name, file_name


## ==============================
## MAIN FUNCTION
## ==============================
def main() -> None:
    """
    Main entry point for the script.
    """
    try:
        ## ✅ Handle Debugger Arguments (Optional for Debugging Tools)
        folder_name, file_name = parse_arguments()

        ## ✅ Execute Function for Folder and File Creation
        print(f"✅ Usage: file_manager.py '{folder_name}' '{file_name}'")
        create_folder_and_file(folder_name, file_name)
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
