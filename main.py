import sys
from pathlib import Path

VERSION = "1.0.1"

def convert_to_markdown(file_path: str) -> str:
    from markitdown import MarkItDown

    source_file = Path(file_path)

    if not source_file.exists():
        raise FileNotFoundError(f"File not found: {source_file}")

    md = MarkItDown()
    result = md.convert(str(source_file))

    output_file = source_file.with_suffix(".md")

    if output_file == source_file:
        output_file = source_file.with_name(
            f"{source_file.stem}_converted.md"
        )

    output_file.write_text(result.text_content, encoding="utf-8")

    return str(output_file)


def print_help():
    print("""
tomd - Convert files to Markdown

USAGE:
  tomd <file>        Convert file to markdown
  tomd -h, --help    Show help
  tomd -v, --version Show version
""")


def print_version():
    print(f"tomd version {VERSION}")

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        print_help()
        sys.exit(0)

    command = args[1]

    if command in ["-h", "--help"]:
        print_help()

    elif command in ["-v", "--version"]:
        print_version()

    else:
        try:
            output = convert_to_markdown(command)
            print(f"Markdown saved to: {output}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)