#!/usr/bin/env python3
"""
Unit tests for file_manager.py.

Author: Python Developer
Date: 2025-01-05
Version: 2.0.0

Purpose:
    Test all utility functions from `file_manager.py` for robustness and correctness.
"""

import pytest
from pathlib import Path
from runbooks.file_manager import (
    create_folder_and_file,
    parse_arguments,
    validate_input,
    validate_folder_name,
    validate_file_name,
)

## ==============================
## TEST: validate_input()
## ==============================
def test_validate_input_valid():
    """Tests valid numeric inputs."""
    assert validate_input(10) == 10.0
    assert validate_input(5.5) == 5.5
    assert validate_input("10") == 10.0
    assert validate_input("5.5") == 5.5


def test_validate_input_invalid_type():
    """Tests invalid input types."""
    with pytest.raises(TypeError, match="Invalid type 'list'. Expected str, int, or float."):
        validate_input([])  # Invalid type (list)

    with pytest.raises(TypeError, match="Invalid type 'dict'. Expected str, int, or float."):
        validate_input({})  # Invalid type (dict)


def test_validate_input_empty_string():
    """Tests empty string handling."""
    with pytest.raises(ValueError, match="Input cannot be empty or whitespace-only."):
        validate_input("")  # Empty string input

    with pytest.raises(ValueError, match="Input cannot be empty or whitespace-only."):
        validate_input("   ")  # Whitespace-only input


def test_validate_input_invalid_number():
    """Tests invalid numeric string."""
    with pytest.raises(ValueError, match="Invalid input 'abc'. Must be a valid number."):
        validate_input("abc")  # Non-numeric string


## ==============================
## TEST: validate_folder_name()
## ==============================
def test_validate_folder_name_valid():
    """Tests valid folder names."""
    validate_folder_name("folder1")
    validate_folder_name("MyFolder_123")


def test_validate_folder_name_invalid():
    """Tests invalid folder names."""
    with pytest.raises(ValueError, match="Folder name cannot be empty."):
        validate_folder_name("")  # Empty name

    with pytest.raises(ValueError, match="Folder name exceeds maximum length"):
        validate_folder_name("a" * 256)  # Exceeding max length

    with pytest.raises(ValueError, match="contains invalid characters."):
        validate_folder_name("folder*")  # Invalid character '*'

    with pytest.raises(ValueError, match="is a reserved keyword."):
        validate_folder_name("CON")  # Reserved Windows keyword

    with pytest.raises(ValueError, match="cannot start or end with spaces."):
        validate_folder_name(" folder ")  # Leading and trailing spaces


## ==============================
## TEST: validate_file_name()
## ==============================
def test_validate_file_name_valid():
    """Tests valid file names."""
    validate_file_name("file.txt")
    validate_file_name("readme.md")


def test_validate_file_name_invalid():
    """Tests invalid file names."""
    with pytest.raises(ValueError, match="File name cannot be empty."):
        validate_file_name("")  # Empty name

    with pytest.raises(ValueError, match="exceeds maximum length"):
        validate_file_name("a" * 256)  # Exceeding max length

    with pytest.raises(ValueError, match="contains invalid characters."):
        validate_file_name("file*?.txt")  # Invalid characters

    with pytest.raises(ValueError, match="cannot start or end with spaces."):
        validate_file_name(" file.txt ")  # Leading and trailing spaces

    with pytest.raises(ValueError, match="must include a valid extension"):
        validate_file_name("filename")  # No extension


## ==============================
## TEST: create_folder_and_file()
## ==============================
@pytest.fixture
def cleanup_test_files():
    """Fixture to clean up created files and folders after tests."""
    yield
    folder_path = Path("test_folder")
    if folder_path.exists():
        for file in folder_path.iterdir():
            file.unlink()
        folder_path.rmdir()


def test_create_folder_and_file_valid(cleanup_test_files):
    """Tests creating folder and file."""
    create_folder_and_file("test_folder", "test_file.txt")
    assert Path("test_folder").exists()
    assert Path("test_folder/test_file.txt").exists()


def test_create_folder_and_file_existing_folder(cleanup_test_files):
    """Tests behavior when folder already exists."""
    Path("test_folder").mkdir()
    create_folder_and_file("test_folder", "new_file.txt")
    assert Path("test_folder/new_file.txt").exists()


def test_create_folder_and_file_existing_file(cleanup_test_files):
    """Tests error handling when file already exists."""
    Path("test_folder").mkdir()
    Path("test_folder/test_file.txt").touch()
    with pytest.raises(FileExistsError, match="File 'test_file.txt' already exists in 'test_folder'"):
        create_folder_and_file("test_folder", "test_file.txt")


def test_create_folder_and_file_invalid_names():
    """Tests error handling for invalid names."""
    with pytest.raises(ValueError, match="contains invalid characters."):
        create_folder_and_file("folder*", "file.txt")

    with pytest.raises(ValueError, match="contains invalid characters."):
        create_folder_and_file("test_folder", "file*?.txt")


## ==============================
## TEST: parse_arguments()
## ==============================
def test_parse_arguments_valid(monkeypatch):
    """Tests valid arguments."""
    monkeypatch.setattr('sys.argv', ["file_manager.py", "folder1", "file1.txt"])
    folder_name, file_name = parse_arguments()
    assert folder_name == "folder1"
    assert file_name == "file1.txt"


def test_parse_arguments_debugger_mode(monkeypatch):
    """Tests debugger mode arguments."""
    monkeypatch.setattr('sys.argv', ["file_manager.py", "folder1 file1.txt"])
    folder_name, file_name = parse_arguments()
    assert folder_name == "folder1"
    assert file_name == "file1.txt"


def test_parse_arguments_invalid(monkeypatch):
    """Tests invalid arguments."""
    monkeypatch.setattr('sys.argv', ["file_manager.py"])
    with pytest.raises(ValueError, match="Provide exactly 2 arguments: <folder_name> <file_name>"):
        parse_arguments()

