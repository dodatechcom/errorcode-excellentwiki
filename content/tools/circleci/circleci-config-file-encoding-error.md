---
title: "[Solution] CircleCI Config File Encoding Error"
description: "Fix CircleCI config file encoding errors when config.yml contains non-UTF-8 characters or BOM markers that prevent parsing."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Config File Encoding Error

Config file encoding errors occur when `.circleci/config.yml` contains non-UTF-8 characters, byte order marks (BOM), or invisible Unicode characters that cause parsing failures.

## Common Causes

- File was edited on Windows with CRLF line endings
- BOM marker was added by a text editor
- Copy-pasted content includes invisible Unicode characters
- YAML comments contain non-ASCII characters in an encoding the parser cannot handle

## How to Fix

### Solution 1: Convert to UTF-8 without BOM

```bash
# Remove BOM marker
sed -i '1s/^\xEF\xBB\xBF//' .circleci/config.yml

# Convert line endings to LF
sed -i 's/\r$//' .circleci/config.yml
```

### Solution 2: Validate encoding

```bash
# Check file encoding
file .circleci/config.yml
# Should show: ASCII text or UTF-8 Unicode text

# Check for non-ASCII characters
cat -v .circleci/config.yml | grep -P '[^\x00-\x7F]'
```

### Solution 3: Re-save with a plain text editor

Open the file in a plain text editor and save as UTF-8 without BOM.

## Examples

```
Error: Invalid YAML syntax: unexpected character
ERROR: config.yml contains non-UTF-8 characters
```

## Prevent It

- Use editors configured for UTF-8 without BOM
- Add `.editorconfig` to enforce encoding:

```ini
[*]
charset = utf-8
end_of_line = lf
```

