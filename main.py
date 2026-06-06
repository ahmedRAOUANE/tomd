from pathlib import Path
from markitdown import MarkItDown


def convert_to_markdown(file_path: str) -> str:
    """
    Convert a file to Markdown and save it next to the original file.

    Example:
        report.pdf -> report.md
        document.docx -> document.md

    Returns the path of the generated markdown file.
    """

    source_file = Path(file_path)

    if not source_file.exists():
        raise FileNotFoundError(f"File not found: {source_file}")

    md = MarkItDown()

    result = md.convert(str(source_file))

    output_file = source_file.with_suffix(".md")

    # If the source is already .md, avoid overwriting
    if output_file == source_file:
        output_file = source_file.with_name(
            f"{source_file.stem}_converted.md"
        )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.text_content)

    return str(output_file)


if __name__ == "__main__":
    file_path = input("Enter the local file path: ").strip()

    try:
        output_path = convert_to_markdown(file_path)
        print(f"Markdown saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")