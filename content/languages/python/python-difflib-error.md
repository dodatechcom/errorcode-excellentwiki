---
title: "[Solution] Python difflib Error — Sequence Comparison Failures"
description: "Fix Python difflib errors including SequenceMatcher, unified_diff, context_diff, get_close_matches, and output mismatches. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 250
---

# Python difflib Error — Sequence Comparison Failures

The `difflib` module provides classes and functions for comparing sequences, especially text lines. Errors occur when comparing incompatible types, using incorrect arguments, or when output formatting fails due to unexpected input.

## Common Causes

```python
# Cause 1: Comparing incompatible sequence types
from difflib import SequenceMatcher

# Comparing lists with different element types
a = [1, "two", 3]
b = ["one", 2, "three"]
sm = SequenceMatcher(None, a, b)
# May produce unexpected ratio due to mixed types

# Cause 2: Empty sequences causing division by zero
from difflib import SequenceMatcher

sm = SequenceMatcher(None, "", "hello")
ratio = sm.ratio()  # Returns 0.0 — but unexpected in some contexts

# Cause 3: get_close_matches with wrong parameters
from difflib import get_close_matches

words = ["apple", "apricot", "avocado", "banana"]
matches = get_close_matches("app", words, n=2, cutoff=0.9)  # Empty list — cutoff too high

# Cause 4: unified_diff with non-string elements
from difflib import unified_diff

a = [1, 2, 3]
b = [1, 2, 4]
diff = list(unified_diff(a, b))  # TypeError: unsupported operand type(s)

# Cause 5: context_diff with wrong lineterm
from difflib import context_diff

a = ["line1\n", "line2\n"]
b = ["line1\n", "line3\n"]
diff = list(context_diff(a, b, lineterm=""))  # Lines may not display correctly
```

## How to Fix

### Fix 1: Use SequenceMatcher correctly

```python
from difflib import SequenceMatcher

def compare_sequences(seq1, seq2):
    sm = SequenceMatcher(None, seq1, seq2)

    # Get matching blocks
    matches = sm.get_matching_blocks()
    print(f"Matching blocks: {matches}")

    # Get ratio (0.0 to 1.0)
    ratio = sm.ratio()
    print(f"Similarity ratio: {ratio:.2%}")

    # Get opcodes for detailed comparison
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        print(f"{tag}: seq1[{i1}:{i2}] -> seq2[{j1}:{j2}]")

compare_sequences("abcde", "abdce")
```

### Fix 2: Handle empty sequences

```python
from difflib import SequenceMatcher

def safe_ratio(seq1, seq2):
    if not seq1 and not seq2:
        return 1.0  # Both empty — considered identical
    if not seq1 or not seq2:
        return 0.0  # One empty — no similarity
    sm = SequenceMatcher(None, seq1, seq2)
    return sm.ratio()

print(safe_ratio("", ""))    # 1.0
print(safe_ratio("abc", ""))  # 0.0
print(safe_ratio("abc", "abc"))  # 1.0
```

### Fix 3: Use get_close_matches with appropriate cutoff

```python
from difflib import get_close_matches

words = ["apple", "apricot", "avocado", "banana", "cherry"]

# Adjust cutoff based on tolerance
close = get_close_matches("apple", words, n=3, cutoff=0.6)
print(f"Cutoff 0.6: {close}")  # ['apple', 'apricot', 'avocado']

close = get_close_matches("apple", words, n=3, cutoff=0.9)
print(f"Cutoff 0.9: {close}")  # ['apple']

# Fuzzy matching for user input
def suggest_corrections(user_input, dictionary, n=5):
    return get_close_matches(user_input, dictionary, n=n, cutoff=0.5)

suggestions = suggest_corrections("banan", words)
print(suggestions)
```

### Fix 4: Convert non-string types for diff

```python
from difflib import unified_diff

# Convert integers to strings before diffing
a = [1, 2, 3, 4]
b = [1, 2, 4, 5]

a_str = [str(x) for x in a]
b_str = [str(x) for x in b]

diff = list(unified_diff(a_str, b_str, lineterm=""))
for line in diff:
    print(line)
```

### Fix 5: Configure diff output correctly

```python
from difflib import unified_diff, context_diff

a = ["line1\n", "line2\n", "line3\n"]
b = ["line1\n", "line3\n", "line4\n"]

# Unified diff with context
diff = unified_diff(
    a, b,
    fromfile="original.txt",
    tofile="modified.txt",
    lineterm="",
    n=3  # Context lines
)
print("\n".join(diff))

# Context diff
diff = context_diff(
    a, b,
    fromfile="original.txt",
    tofile="modified.txt",
    lineterm=""
)
print("\n".join(diff))

# HTML diff for web output
from difflib import HtmlDiff

differ = HtmlDiff()
html_diff = differ.make_file(a, b, fromdesc="Original", todesc="Modified")
print(html_diff[:200])
```

## Examples

```python
# Real-world: Compare two files line by line
from difflib import SequenceMatcher, unified_diff

def compare_files(file1, file2):
    with open(file1) as f1:
        lines1 = f1.readlines()
    with open(file2) as f2:
        lines2 = f2.readlines()

    sm = SequenceMatcher(None, lines1, lines2)
    ratio = sm.ratio()
    print(f"Files are {ratio:.1%} similar")

    diff = list(unified_diff(lines1, lines2,
                             fromfile=file1, tofile=file2))
    if diff:
        print("Differences:")
        print("".join(diff))
    else:
        print("Files are identical")

# Real-world: Find closest match in a list
from difflib import get_close_matches

def find_closest(word, wordlist, n=3):
    matches = get_close_matches(word, wordlist, n=n, cutoff=0.4)
    if matches:
        return matches[0]
    return None

database = ["postgresql", "mysql", "mongodb", "redis", "sqlite"]
print(find_closest("postgress", database))  # postgresql
print(find_closest("mysequel", database))   # mysql
```

## Related Errors

- [TypeError](/languages/python/typeerror/) — comparing incompatible types
- [ValueError](/languages/python/valueerror/) — invalid function arguments
- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — encoding issues in file comparison
