import sys
from pathlib import Path

VERSION = "1.2.6"

def save_file(source_file: str, content: str)->str:
    output_file = Path(source_file).with_suffix(".md")

    if output_file == source_file:
        output_file = source_file.with_name(
            f"{source_file.stem}_converted.md"
        )

    output_file.write_text(content, encoding="utf-8")

    return str(output_file)

def convert_to_markdown(file_path: str) -> str:
    from markitdown import MarkItDown

    source_file = Path(file_path)

    if not source_file.exists():
        raise FileNotFoundError(f"File not found: {source_file}")

    md = MarkItDown()
    return md.convert(str(source_file)).text_content

def print_help():
    print("""
tomd - Convert files to Markdown

USAGE:
  tomd <file>                    Convert file to markdown
  tomd -h, --help                Show help
  tomd -v, --version             Show version
  tomd --compact <file>          optimize the output file
  tomd --log                     print logs, you use it with --compact to see how much you've reduced
""")

def print_version():
    print(f"tomd version {VERSION}")

if __name__ == "__main__":
    args = sys.argv

    flags = set(args[1:])

    help_mode = "-h" in flags or "--help" in flags
    version_mode = "-v" in flags or "--version" in flags
    compact_mode = "--compact" in flags
    log_mode = "--log" in flags

    file_path = None

    for arg in args[1:]:
        if not arg.startswith("-"):
            file_path = arg
            break

    if help_mode:
        print_help()
        sys.exit(0)

    if version_mode:
        print_version()
        sys.exit(0)

    if file_path is None:
        print("Error: No file specified")
        print_help()
        sys.exit(1)

    try:
        md_content = convert_to_markdown(file_path)

        if compact_mode:
            from optimizer import optimize_markdown

            optimized_md, stats = optimize_markdown(md_content)

            output_file = save_file(
                file_path,
                optimized_md
            )

            print(
                f"Optimized Markdown for LLM saved to: {output_file}"
            )

            if log_mode:
                from optimizer import print_optimization_stats
                
                print_optimization_stats(
                    md_content,
                    optimized_md,
                    stats
                )

        else:
            output_file = save_file(
                file_path,
                md_content
            )

            print(f"Markdown saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

