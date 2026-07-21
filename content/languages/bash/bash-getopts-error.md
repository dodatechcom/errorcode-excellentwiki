---
title: "[Solution] Bash Getopts Error -- Incorrect Option Parsing"
description: "Fix bash getopts errors when parsing command-line options with the getopts builtin."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Getopts Error

This error occurs when the `getopts` builtin is used with incorrect option strings or handling.

## Common Causes

- Option string missing `:` for required arguments
- Not handling `?` for unknown options
- Using getopts with long options (it only handles short options)
- Missing `:` before option argument specification

## How to Fix

### Use correct getopts syntax

```bash
# WRONG: no : for argument
while getopts "fv" opt; do
    case "$opt" in
        f) FILE="$OPTARG";;  # OPTARG not set
    esac
done

# CORRECT: : after option that takes argument
while getopts "f:v" opt; do
    case "$opt" in
        f) FILE="$OPTARG";;
        v) VERBOSE=1;;
        \?) echo "Invalid option"; exit 1;;
    esac
done
```

## Examples

```bash
#!/bin/bash
while getopts "h:p:v" opt; do
    case "$opt" in
        h) HOST="$OPTARG";;
        p) PORT="$OPTARG";;
        v) VERBOSE=1;;
        \?) usage; exit 1;;
    esac
done
```
