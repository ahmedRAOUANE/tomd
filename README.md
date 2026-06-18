# To-Markdown

A Python utility that converts various file formats into Markdown (.md) files.

## Overview

**To-Markdown** is a simple command-line tool that takes files in different formats (PDF, DOCX, XLSX, PPTX, etc.) and converts them to Markdown format. It leverages the `MarkItDown` library to handle the conversion process.

## Features

- Convert multiple file formats to Markdown
- Automatic file naming (e.g., `report.pdf` → `report.md`)
- Handles edge cases (e.g., if source is already `.md`, saves as `[filename]_converted.md`)
- Error handling for missing or invalid files
- UTF-8 encoded output
- `--compact` command for optization
- `--log` command gives you a detailed report about how much tokens you saved

## How It Works

1. User provides the path to a source file
2. The tool reads the file using MarkItDown
3. Converts the content to Markdown format
4. Saves the output as a `.md` file in the same directory as the source file

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. Clone or download this project to your local machine

2. Navigate to the project directory:
   ```bash
   cd tomd
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python main.py
```

When prompted, enter the full path to the file you want to convert:
```
Enter the local file path: C:\path\to\your\document.pdf
```

The tool will convert the file and display the path to the generated Markdown file:
```
Markdown saved to: C:\path\to\your\document.md
```

## Example
- in developement
```bash
python main.py file path: /Users/user/Documents/report.docx
Markdown saved to: /Users/user/Documents/report.md
```
- in production
```bash
  tomd <path to file>            Convert file to markdown
  tomd -h, --help                Show help
  tomd -v, --version             Show version
  tomd --compact <path to file>  optimize the output file
  tomd --log                     print logs, you use it with --compact to see how much you've reduced
```

## Error Handling

The tool handles common errors gracefully:
- **File not found**: Displays an error if the specified file doesn't exist
- **Invalid path**: Handles path validation and user input errors
- **Existing files**: If converting a `.md` file, saves as `[filename]_converted.md` to avoid overwriting

## Dependencies

See `requirements.txt` for the list of required packages. The main dependency is:
- `MarkItDown`: Library for converting various document formats to Markdown

## Packaging
- 1. run the command 
`pyinstaller --onedir --clean --name tomd main.py`
this will create a `dist/tomd/` folder
- 2. open `setup.iss` with [inno setup](https://jrsoftware.org/isdl.php/Inno-Setup-Downloads) and run the script this should create `Output/tomd_setup.exe` file

## License

This project is available for personal and commercial use.
