---
title: "[Solution] Bash Process Substitution Failed Error"
description: "Fix 'process substitution failed' in Bash when <() or >() syntax fails."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash Process Substitution Failed Error Fix

This error occurs when Bash cannot create a file descriptor for process substitution using `<()` or `>()`.

## Description

Process substitution lets you treat a command's output (or input) as a file. Bash creates a temporary file descriptor and runs the command asynchronously. When the system runs out of file descriptors or the command fails to start, this error occurs.

## Common Causes

- **File descriptor exhaustion** — too many open files or process substitutions.
- **Command doesn't exist** — the process inside `<()` can't be executed.
- **Pipe or FIFO failure** — system can't create the named pipe.
- **Running too many parallel substitutions** — resource limits hit.

## How to Fix

### Fix 1: Increase file descriptor limits

```bash
# Check current limit
ulimit -n

# Increase temporarily
ulimit -n 4096
```

### Fix 2: Close unused file descriptors

```bash
# Open and close within a function
run_process() {
    exec 3< <(some_command)
    # Use fd 3
    cat <&3
    exec 3<&-  # Close fd 3
}
```

### Fix 3: Verify the command inside process substitution exists

```bash
# Check before using
if command -v mycommand &>/dev/null; then
    diff <(mycommand file1) <(mycommand file2)
else
    echo "mycommand not found"
fi
```

### Fix 4: Use alternative approaches for resource-constrained environments

```bash
# Instead of
diff <(cmd1) <(cmd2)

# Use temporary files
cmd1 > /tmp/out1.txt
cmd2 > /tmp/out2.txt
diff /tmp/out1.txt /tmp/out2.txt
rm -f /tmp/out1.txt /tmp/out2.txt
```

## Examples

```bash
$ diff <(ls dir1) <(ls dir2)
# Works if both directories exist

$ diff <(nonexistent_command) <(ls /tmp)
bash: process substitution failed: nonexistent_command

$ # Too many open file descriptors
for i in $(seq 1 10000); do
    echo "test" | cat <(echo "$i")
done
```

## Related Errors

- [No Such File or Directory](no-such-file) — command inside substitution doesn't exist.
- [Pipe Failure](pipe-failure) — issues with pipes and file descriptors.
