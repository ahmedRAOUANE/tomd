import re

def print_optimization_stats(
    original: str,
    optimized: str,
    stats: dict
):
    original_chars = len(original)
    optimized_chars = len(optimized)

    saved_chars = original_chars - optimized_chars

    reduction = (
        (saved_chars / original_chars) * 100
        if original_chars > 0
        else 0
    )

    original_tokens = original_chars // 4
    optimized_tokens = optimized_chars // 4
    saved_tokens = original_tokens - optimized_tokens

    print("\nOptimization Statistics")
    print("-" * 25)
    print(f"Original size : {original_chars:,} chars")
    print(f"Optimized size: {optimized_chars:,} chars")
    print(f"Saved         : {saved_chars:,} chars")
    print(f"Reduction     : {reduction:.1f}%")
    print()
    print(f"Estimated tokens before: {original_tokens:,}")
    print(f"Estimated tokens after : {optimized_tokens:,}")
    print(f"Estimated tokens saved : {saved_tokens:,}")
    print()
    for item in stats:
        print(str(item).replace("_", " "), stats[item])


def optimize_markdown(text: str):
    stats = {}

    text, control_stats = remove_control_chars(text)
    stats.update(control_stats)

    text = normalize_whitespace(text)
    text = merge_broken_lines(text)
    text = collapse_blank_lines(text)

    return text, stats


def remove_control_chars(text: str) -> str:
    fcount = text.count("\f")
    vcount = text.count("\v")

    text = text.replace("\f", "")
    text = text.replace("\v", "")

    return text, {
        "form_feeds_removed": fcount,
        "vertical_tabs_removed": vcount,
    }


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


