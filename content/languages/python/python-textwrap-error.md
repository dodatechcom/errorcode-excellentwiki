---
title: "[Solution] Python textwrap Module Error — Text Wrapping and Indentation Failures"
description: "Fix Python textwrap module errors including wrap/fill/dedent, indent, TextWrapper, and placeholder errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 255
---

# Python textwrap Module Error — Text Wrapping and Indentation Failures

The `textwrap` module provides functions for wrapping and formatting plain text. Errors occur when width parameters are too small, indentation is inconsistent, or placeholder strings conflict with existing text.

## Common Causes

```python
# Cause 1: Width smaller than longest word
import textwrap

result = textwrap.wrap("supercalifragilisticexpialidocious", width=10)
# ['supercalif', 'ragilistic', 'expialidoc', 'ious'] — breaks words

# Cause 2: Placeholder in indent conflicts with text
import textwrap

result = textwrap.indent("hello world", "> ")
# 'hello world' — indent doesn't handle existing indentation

# Cause 3: fill() with empty string
import textwrap

result = textwrap.fill("", width=20)
# Returns '' — unexpected in some contexts

# Cause 4: dedent with inconsistent indentation
import textwrap

text = "  line1\n    line2\n  line3"
result = textwrap.dedent(text)
# Inconsistent: "  line1\n    line2\n  line3" — only common whitespace removed

# Cause 5: TextWrapper with invalid parameters
import textwrap

wrapper = textwrap.TextWrapper(width=-1)  # No error, but produces empty lines
result = wrapper.wrap("Hello world")
# [] — negative width produces nothing
```

## How to Fix

### Fix 1: Control word wrapping with break_long_words

```python
import textwrap

# Break long words (default behavior)
result = textwrap.wrap("supercalifragilisticexpialidocious", width=10, break_long_words=True)
print(result)  # ['supercalif', 'ragilistic', 'expialidoc', 'ious']

# Don't break long words — they overflow
result = textwrap.wrap("supercalifragilisticexpialidocious", width=10, break_long_words=False)
print(result)  # ['supercalifragilisticexpialidocious']

# Break on hyphens
result = textwrap.wrap("well-known example", width=10, break_on_hyphens=True)
print(result)  # ['well-known', 'example']
```

### Fix 2: Use indent with proper predicate

```python
import textwrap

text = "line1\n  line2\nline3"

# Default: only add indent to non-blank lines
result = textwrap.indent(text, ">> ")
print(result)
# >> line1
# >>   line2
# >> line3

# Custom predicate — indent all lines
result = textwrap.indent(text, ">> ", predicate=lambda line: True)
print(result)
# >> line1
# >>   line2
# >> line3

# Strip then indent
result = textwrap.indent(text.strip(), ">> ")
print(result)
# >> line1
# >>   line2
# >> line3
```

### Fix 3: Use dedent for consistent indentation

```python
import textwrap

text = """\
    line1
        line2
    line3"""

# dedent removes common leading whitespace
result = textwrap.dedent(text)
print(result)
# line1
#     line2
# line3

# Combine dedent with indent for consistent formatting
def normalize_indentation(text, indent="    "):
    return textwrap.indent(textwrap.dedent(text), indent)

result = normalize_indentation(text, indent="  ")
print(result)
#   line1
#     line2
#   line3
```

### Fix 4: Configure TextWrapper for complex cases

```python
import textwrap

wrapper = textwrap.TextWrapper(
    width=40,
    initial_indent="  ",
    subsequent_indent="    ",
    break_long_words=True,
    break_on_hyphens=True,
    max_lines=3,
    placeholder="..."
)

text = "This is a long text that should be wrapped properly with indentation and overflow handling."
result = wrapper.fill(text)
print(result)
#   This is a long text that
#       should be wrapped
#       properly...
```

### Fix 5: Handle fill() edge cases

```python
import textwrap

def safe_fill(text, width=70, **kwargs):
    if not text:
        return ""
    # Strip leading/trailing whitespace
    text = text.strip()
    if not text:
        return ""
    return textwrap.fill(text, width=width, **kwargs)

# Edge cases
print(safe_fill(""))           # ""
print(safe_fill("  "))         # ""
print(safe_fill("hello"))      # hello
print(safe_fill("a" * 100, width=20))  # Wrapped long string
```

## Examples

```python
# Real-world: Format help text for CLI
import textwrap

def format_help(command, description, options, width=80):
    lines = [f"Usage: {command}"]
    lines.append("")
    lines.append(textwrap.fill(description, width=width))
    lines.append("")
    lines.append("Options:")

    for opt, desc in options.items():
        opt_text = f"  {opt:<20} {desc}"
        wrapped = textwrap.fill(opt_text, width=width,
                               subsequent_indent=" " * 22)
        lines.append(wrapped)

    return "\n".join(lines)

help_text = format_help(
    "myapp",
    "A tool for processing data files.",
    {"--input": "Input file path",
     "--output": "Output file path (default: stdout)",
     "--verbose": "Enable verbose output"}
)
print(help_text)

# Real-world: Indent code blocks for display
import textwrap

def indent_code(code, language="python"):
    dedented = textwrap.dedent(code).strip()
    indented = textwrap.indent(dedented, "    ")
    return f"```{language}\n{indented}\n```"

code = """
def hello():
    print("Hello, World!")
"""
print(indent_code(code))
```

## Related Errors

- [ValueError](/languages/python/valueerror/) — invalid width or parameters
- [TypeError](/languages/python/typeerror/) — wrong argument types
- [IndexError](/languages/python/indexerror/) — accessing wrapped result incorrectly
