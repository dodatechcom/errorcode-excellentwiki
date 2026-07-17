---
title: "[Solution] Bash Process Substitution Failed Error Fix"
description: "Fix bash process substitution errors when <() or >() fails."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Process Substitution Failed Error Fix

A bash process substitution error occurs when `<()` or `>`() fails to create the temporary file descriptor needed for the process.

## What This Error Means

Process substitution `<()` runs a command and connects its output to a file descriptor, allowing you to use it like a file. It fails when the system can't create the needed file descriptors (e.g., on some non-Linux systems or when /dev/fd is unavailable).

## Common Causes

- `/dev/fd` not available on the system
- Too many open file descriptors
- Command inside `<()` fails immediately
- Using process substitution on non-Linux systems (macOS may need bash from Homebrew)

## How to Fix

### 1. Use process substitution correctly

```bash
# WRONG: Command inside <() fails
diff <(ls /nonexistent) <(ls /tmp)

# CORRECT: Ensure commands succeed
diff <(ls /tmp) <(sorted_list)
```

### 2. Use temp files as fallback

```bash
# CORRECT: Use temp files when process substitution unavailable
tmp1=$(mktemp)
tmp2=$(mktemp)
command1 > "$tmp1"
command2 > "$tmp2"
diff "$tmp1" "$tmp2"
rm -f "$tmp1" "$tmp2"
```

### 3. Compare files with process substitution

```bash
# CORRECT: Common pattern — compare outputs
diff <(sort file1.txt) <(sort file2.txt)
diff <(git log --oneline main) <(git log --oneline dev)
```

### 4. Use with while read

```bash
# CORRECT: Feed multiple commands to while
while read -r line; do
    echo "$line"
done < <(command1; command2)
```

## Related Errors

- [Bash Pipe Error](bash-pipe-error) — pipe failures
- [No Such File](no-such-file) — missing files
- [Permission Denied](permission-denied) — access errors
