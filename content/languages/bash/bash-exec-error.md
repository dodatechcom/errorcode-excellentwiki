---
title: "[Solution] Bash Exec Command Not Found Error Fix"
description: "Fix 'exec: not found' in Bash. Resolve command execution failures when using exec to replace shell processes."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Exec Command Not Found Error Fix

The `exec: not found` error occurs when the `exec` command cannot find the specified executable in the system PATH or at the given path.

## What This Error Means

The `exec` command replaces the current shell process with the specified command. When the command does not exist, is not in PATH, or the path is incorrect, Bash reports the error. Unlike normal command execution, `exec` failures can leave the shell in an inconsistent state.

A typical error:

```
bash: exec: mycommand: not found
```

## Why It Happens

Common causes include:

- **Command not installed** — The program is not present on the system.
- **Not in PATH** — The executable exists but PATH does not include its directory.
- **Typo in command name** — Misspelling the command.
- **Wrong absolute path** — Using an incorrect full path to the binary.
- **Script not executable** — `exec script.sh` when the script lacks `+x` permission.

## How to Fix It

### Fix 1: Verify the command exists

```bash
# Check if command is available
which mycommand || echo "not found"

# Or use type
type mycommand

# Search for it
find / -name "mycommand" 2>/dev/null
```

### Fix 2: Use full absolute path

```bash
# WRONG: Relying on PATH
exec mycommand --flag

# RIGHT: Use absolute path
exec /usr/local/bin/mycommand --flag
```

### Fix 3: Update PATH if needed

```bash
# Add custom directory to PATH
export PATH="/opt/myapp/bin:$PATH"
exec mycommand --flag
```

### Fix 4: Check script permissions

```bash
# Make script executable
chmod +x /path/to/script.sh

# Then exec it
exec /path/to/script.sh
```

### Fix 5: Use exec with error handling

```bash
# RIGHT: Check before exec
if command -v mycommand &> /dev/null; then
    exec mycommand "$@"
else
    echo "Error: mycommand not found" >&2
    exit 1
fi
```

## Common Mistakes

- **Forgetting that exec replaces the current process** — The shell script stops after exec.
- **Assuming exec inherits environment correctly** — Environment is inherited but PATH may be wrong.
- **Using exec in subshells unnecessarily** — Use direct command invocation in subshells.

## Related Pages

- [Bash Source Error](bash-source-error) — File not found when sourcing
- [Bash Builtin Error](bash-builtin-error) — Shell builtin errors
- [Bash Recursive Descent](bash-recursive-descent) — Stack overflow issues
