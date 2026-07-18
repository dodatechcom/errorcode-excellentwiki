---
title: "[Solution] Bash Getopts Illegal Option Error Fix"
description: "Fix 'getopts: illegal option' in Bash. Resolve option string format issues and unsupported option flags in scripts."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Getopts Illegal Option Error Fix

The `getopts: illegal option` error occurs when an option character passed to the script is not listed in the option string.

## What This Error Means

The `getopts` built-in parses command-line options based on a specification string. If a user passes an option not defined in that string, getopts reports an illegal option error and sets the option variable to `?`.

A typical error:

```
getopts: illegal option -- x
```

## Why It Happens

Common causes include:

- **Option not in the option string** — User passes `-x` when only `-f:v` is defined.
- **Missing colon for required arguments** — `f` instead of `f:` means `-f` takes no argument.
- **Wrong option string format** — Spaces, commas, or special characters in the string.
- **Processing `-` or `--`** — Bare dashes are not handled by getopts.
- **Positional parameters already shifted** — Getopts processes `$@` from wrong position.

## How to Fix It

### Fix 1: Define all supported options

```bash
# RIGHT: Include all valid options
while getopts "f:vh" opt; do
    case "$opt" in
        f) FILE="$OPTARG" ;;
        v) VERBOSE=1 ;;
        h) usage; exit 0 ;;
        \?) echo "Invalid option: -$OPTARG" >&2; exit 1 ;;
        :) echo "Option -$OPTARG requires an argument" >&2; exit 1 ;;
    esac
done
```

### Fix 2: Handle the error case properly

```bash
# RIGHT: Use \? and : in case statement
while getopts "ab:c" opt; do
    case "$opt" in
        a) echo "Option a" ;;
        b) echo "Option b with arg: $OPTARG" ;;
        c) echo "Option c" ;;
        \?) echo "Unknown option -$OPTARG" >&2; exit 1 ;;
        :) echo "Option -$OPTARG requires an argument" >&2; exit 1 ;;
    esac
done
```

### Fix 3: Correct option string syntax

```bash
# WRONG: Using commas
getopts "f,v,h" opt  # WRONG

# WRONG: Using spaces
getopts "f v h" opt  # WRONG

# RIGHT: Sequential characters, colons for args
getopts "fvh:" opt  # f and v take no args, h takes one
```

### Fix 4: Support GNU-style long options separately

```bash
# getopts does not support long options, parse manually first
while [ $# -gt 0 ]; do
    case "$1" in
        --file) FILE="$2"; shift 2 ;;
        --verbose) VERBOSE=1; shift ;;
        --) shift; break ;;
        -*) break ;;  # Fall through to getopts
        *) break ;;
    esac
done

# Then use getopts for short options
while getopts "f:vh" opt; do
    case "$opt" in
        f) FILE="$OPTARG" ;;
        v) VERBOSE=1 ;;
        h) usage; exit 0 ;;
    esac
done
```

### Fix 5: Shift past processed options

```bash
# RIGHT: Shift past options before processing positional args
while getopts "f:vo:" opt; do
    case "$opt" in
        f) INPUT="$OPTARG" ;;
        v) VERBOSE=1 ;;
        o) OUTPUT="$OPTARG" ;;
    esac
done
shift $((OPTIND - 1))

# Now $1, $2... are positional arguments
echo "File: $INPUT, Output: $OUTPUT"
echo "Remaining args: $@"
```

## Common Mistakes

- **Forgetting the colon for required arguments** — `f:` means `-f value`, `f` means `-f` alone.
- **Not handling `\?` and `:` cases** — Always include error handling.
- **Using getopts for long options** — Use `getopt` (external command) for `--long` options.

## Related Pages

- [Bash Shift Error](bash-shift-error) — Positional parameter shifting
- [Bash While Syntax Error](bash-while-syntax-error) — While loop syntax issues
- [Bash For Syntax Error](bash-for-syntax-error) — For loop syntax errors
