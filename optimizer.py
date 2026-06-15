import re


def optimize_markdown(text: str) -> str:
    text = normalize_whitespace(text)
    text = merge_broken_lines(text)
    text = collapse_blank_lines(text)

    return text


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)

    return "\n".join(
        line.rstrip()
        for line in text.splitlines()
    )


def collapse_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def merge_broken_lines(text: str) -> str:
    lines = text.splitlines()
    result = []

    for line in lines:
        line = line.strip()

        if not line:
            result.append("")
            continue

        if (
            result
            and result[-1]
            and not result[-1].startswith("#")
            and not line.startswith(("#", "-", "*"))
        ):
            result[-1] += " " + line
        else:
            result.append(line)

    return "\n".join(result)