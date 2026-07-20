---
title: "[Solution] Here-String `<<<` Error"
description: "Fix here-string (<<<) errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Here-String `<<<` Error

The here-string operator `<<<` is Bash-specific and has syntax requirements.

### Common Causes
- Using `<<<` in `sh` instead of `bash`.
- Missing the string to pass.
- Unquoted string with spaces.

### How to Fix
```bash
# Ensure bash mode
#!/bin/bash

# Pass string to command via here-string
read -r first rest <<< "hello world"
echo "$first"    # hello

# Quote strings with spaces
read -r a b <<< "one two"
echo "$a $b"    # one two

# Use pipe as fallback
echo "hello world" | read -r first rest
```

### Example
```bash
# Broken (in sh)
read -r var <<< "test"

# Fixed
#!/bin/bash
read -r var <<< "test"
```
