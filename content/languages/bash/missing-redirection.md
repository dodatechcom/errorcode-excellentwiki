---
title: "[Solution] Bash Missing Redirection Error"
description: "Fix 'bash: command not found' caused by incorrect use of output or input redirection operators."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "redirection", "output", "input", "file-descriptor"]
severity: "error"
---

# Missing Redirection

## Error Message

```
bash: command not found: >
```

## Common Causes

- A redirection operator `>` or `<` is placed where Bash expects a command
- Missing the target filename after a redirection operator
- Using `>` without a preceding command, causing Bash to interpret `>` as a command
- Incorrect file descriptor syntax (e.g., `2>&` without the target)

## Solutions

### Solution 1: Place Redirection After the Command

Redirection operators must come after a command. The redirect applies to the command's output or input.

```bash
# Wrong — > has no command before it
> output.txt

# Right — redirect the output of echo
echo "hello" > output.txt

# Wrong — < has no command before it
< input.txt

# Right — use cat or while to read from input
while read -r line; do
    echo "$line"
done < input.txt

# Append mode
echo "another line" >> output.txt 
```

### Solution 2: Provide a Target for Redirection

Every redirection operator needs a target file (or file descriptor). Without it, Bash will produce an error or unexpected behavior.

```bash
# Wrong — missing file after >
echo "data" >

# Right
echo "data" > output.txt

# Wrong — missing file after >>
echo "data" >>

# Right — append to file
echo "data" >> output.txt

# Wrong — incomplete fd redirect
2>&

# Right — redirect stderr to stdout
echo "error" 2>&1

# Redirect both stdout and stderr
command > all_output.txt 2>&1 
```

## Prevention Tips

- Always place redirection operators after a command
- Use `>` to overwrite, `>>` to append, and `<` for input
- Remember: `2>` redirects stderr, `1>` redirects stdout (or just `>`)

## Related Errors

- [Missing Pipe]({< relref "/languages/bash/missing-pipe" >})
- [No Such File]({< relref "/languages/bash/no-such-file" >})
