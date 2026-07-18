---
title: "[Solution] Bash Process Substitution Failed Not Supported Fix"
description: "Fix 'process substitution failed' or 'not supported' in Bash. Enable process substitution and resolve /dev/fd issues."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Process Substitution Failed Not Supported Fix

The `process substitution failed` or `not supported` error occurs when Bash cannot create process substitution using `<()` or `>()`, often due to missing `/dev/fd` support or shell limitations.

## What This Error Means

Process substitution lets you treat command output as a file using `<(command)` for input or `>()` for output. This requires `/dev/fd` or `/proc/self/fd` to be available. When the system lacks this support or the shell is too old, the substitution fails.

A typical error:

```
bash: /dev/fd/63: No such file or directory
```

## Why It Happens

Common causes include:

- **Missing `/dev/fd` support** — Some minimal containers or systems lack `/dev/fd`.
- **Using Bash 3 or older** — Process substitution requires Bash 4.0+.
- **Shells other than Bash** — `sh`, `dash`, and `zsh` may not support `<()`.
- **Too many process substitutions** — Running out of file descriptors.
- **Running inside a subshell** — Some environments restrict `/dev/fd`.

## How to Fix It

### Fix 1: Check Bash version

```bash
# Check your Bash version
bash --version

# Process substitution requires Bash 4.0+
# If too old, upgrade or use alternatives
```

### Fix 2: Use temporary files as fallback

```bash
# WRONG: Process substitution not available
diff <(sort file1.txt) <(sort file2.txt)

# RIGHT: Use temporary files
sort file1.txt > /tmp/sorted1.txt
sort file2.txt > /tmp/sorted2.txt
diff /tmp/sorted1.txt /tmp/sorted2.txt
rm -f /tmp/sorted1.txt /tmp/sorted2.txt
```

### Fix 3: Use pipelines instead of process substitution

```bash
# WRONG: Process substitution
while read line; do
    echo "$line"
done < <(grep "error" logfile.txt)

# RIGHT: Use a pipeline
grep "error" logfile.txt | while read line; do
    echo "$line"
done
```

### Fix 4: Install /dev/fd support

```bash
# On Linux, ensure /dev/fd exists
ls -la /dev/fd

# If missing, create symlink
sudo ln -s /proc/self/fd /dev/fd

# Or mount devpts
sudo mount -t devpts devpts /dev/pts
```

### Fix 5: Use bash-specific shebang

```bash
# Ensure the script runs with bash, not sh
#!/bin/bash
# NOT #!/bin/sh

# Then use process substitution
while read -r line; do
    process_line "$line"
done < <(find /var/log -name "*.log" -mtime -1)
```

### Fix 6: Alternative for POSIX shells

```bash
# Use a function to simulate process substitution
process_and_diff() {
    sort "$1" > /tmp/ps_a.txt
    sort "$2" > /tmp/ps_b.txt
    diff /tmp/ps_a.txt /tmp/ps_b.txt
}
process_and_diff file1.txt file2.txt
```

## Common Mistakes

- **Using `#!/bin/sh` on a script with process substitution** — `sh` may be `dash` which lacks support.
- **Assuming process substitution works in Docker containers** — Minimal images may lack `/dev/fd`.
- **Not handling file descriptor limits** — Too many simultaneous substitutions exhaust FDs.

## Related Pages

- [Bash Substitution Error](bash-substitution-error) — Variable substitution issues
- [Bash Bad Substitution](bad-substitution) — Incorrect variable expansion
- [Bash Connection Error](bash-connection-error) — Pipe and redirection errors
