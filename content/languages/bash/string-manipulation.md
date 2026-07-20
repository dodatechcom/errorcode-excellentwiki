---
title: "[Solution] Bash String Manipulation Error"
description: "Fix 'bash: string manipulation error' when using incorrect substring, pattern matching, or string operation syntax."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "strings", "substring", "pattern-matching"]
severity: "error"
---

# String Manipulation Error

## Error Message

```
bash: string manipulation error
```

## Common Causes

- Using invalid syntax for substring extraction (e.g., `${str:offset:length}` with non-numeric values)
- Incorrect pattern matching in `${str/pattern/replacement}`
- Trying to use string operations on undefined variables
- Mixing up Bash string syntax with other shell dialects

## Solutions

### Solution 1: Use Correct Substring and Pattern Syntax

Bash provides many string manipulation operators. Use the correct syntax for each operation and ensure variables are defined before use.

```bash
#!/bin/bash
str="Hello, World!"

# Substring extraction: \${str:offset:length}
echo "${str:0:5}"       # Output: Hello
echo "${str:7}"         # Output: World!
echo "${str: -6}"       # Output: World! (space before - is required)

# Pattern replacement: \${str/pattern/replacement}
echo "${str/World/Bash}" # Output: Hello, Bash!

# Global replacement
echo "${str//l/L}"       # Output: HeLLo, WorLd!

# String length
echo "${#str}"           # Output: 13

# Case conversion (Bash 4+)
echo "${str^^}"          # Output: HELLO, WORLD!
echo "${str,,}"          # Output: hello, world! 
```

### Solution 2: Handle Edge Cases in String Operations

Be careful with empty strings, negative offsets, and patterns that don't match. Always check string length before extracting substrings.

```bash
#!/bin/bash
str="test"

# Check length before substring extraction
if [ "${#str}" -ge 5 ]; then
    echo "${str:0:5}"
else
    echo "String too short: '$str' (${#str} chars)"
fi

# Safe default with substring
filename="archive.tar.gz"
echo "${filename%%.*}"     # Output: archive (remove longest .*)
echo "${filename#*.}"      # Output: tar.gz (remove shortest *.)
echo "${filename%.gz}"     # Output: archive.tar

# Quote variables to handle spaces and special chars
word="hello world"
echo "${word%% *}"         # Output: hello 
```

## Prevention Tips

- Use `${var:offset:length}` for substring extraction
- Use `${var/pattern/replacement}` for pattern replacement
- Always quote variable expansions to handle spaces: `"${var}"`

## Related Errors

- [Parameter Expansion Error]({< relref "/languages/bash/parameter-expansion" >})
- [Variable Substitution Error]({< relref "/languages/bash/variable-substitution" >})
