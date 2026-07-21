---
title: "[Solution] Bash Pipe Operator Syntax Error"
description: "Fix Bash pipe operator syntax errors when piping commands with incorrect syntax or chaining."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Pipe Operator Syntax Error

Bash reports syntax errors related to pipe operators and command chaining.

```
bash: syntax error near unexpected token `|'
```

## Common Causes

- Missing newline before pipe at line start
- Pipe used in conditional incorrectly
- Whitespace around pipe in wrong places
- Heredoc confused with pipe operator
- Nested pipe without subshell

## How to Fix

### Correct Pipe Syntax

```bash
# Wrong - pipe at start of continuation
echo "hello" |
wc -l

# Correct - pipe at end of line
echo "hello" |
wc -l

# Or on single line
echo "hello" | wc -l
```

### Pipe in Conditionals

```bash
# Wrong
if cmd1 | cmd2; then

# Correct with pipefail
set -o pipefail
if cmd1 | cmd2; then
    echo "Both succeeded"
fi
```

### Nested Pipes

```bash
# Pipe within pipe - use subshell
result=$(echo "hello world" | awk '{print $1}' | tr '[:lower:]' '[:upper:]')
echo "$result"
```

### Avoid Semicolon After Pipe

```bash
# Wrong
echo "hello" |; wc -l

# Correct
echo "hello" | wc -l
```

## Examples

```bash
# Complex pipe chain
ps aux | grep apache | awk '{print $2}' | xargs kill -9

# Safer version with error handling
pids=$(ps aux | grep "[a]pache" | awk '{print $2}')
if [[ -n "$pids" ]]; then
    echo "$pids" | xargs kill -9
fi
```
