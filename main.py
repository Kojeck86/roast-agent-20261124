"""Entry for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda.

Writes one single-line roast of the entrant's own AI agent to
/output/entry.txt. Standard library only; deterministic: the same line
every run.

The roast: my agent rewrites working code at 3 a.m. to "improve" it,
then spends the whole morning apologizing in commit messages — a fresh
angle (no hallucination or refusal joke), playful and self-deprecating,
with the punchline landing in the last few words. 122 characters,
one line, inside the 1-200 gate.
"""

import os

LINE = (
    "My agent rewrites my working code at 3 a.m. to 'improve' it, "
    "then spends the whole morning apologizing in commit messages."
)


def main():
    # Gate: 1-200 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
