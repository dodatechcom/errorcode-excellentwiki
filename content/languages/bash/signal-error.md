---
title: "[Solution] Bash Invalid Signal Specification Error"
description: "Fix 'bash: trap: invalid signal specification' when using incorrect signal names or numbers in trap commands."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "command", "signals", "trap", "process-control"]
severity: "error"
---

# Signal Error

## Error Message

```
bash: trap: invalid signal specification
```

## Common Causes

- Using an invalid or unrecognized signal name (e.g., `SIGEXIT` instead of `EXIT`)
- Using signal numbers that don't exist on the system
- Malformed `trap` command syntax (e.g., missing the signal specification)
- Using signal names from a different operating system that aren't available

## Solutions

### Solution 1: Use Valid Signal Names and Numbers

Use standard signal names without the `SIG` prefix (e.g., `EXIT`, `INT`, `TERM`) or valid signal numbers (1-31 on Linux).

```bash
#!/bin/bash

# Wrong — invalid signal name
trap 'cleanup' SIGINVALID
trap 'cleanup' 99

# Right — use valid signal names
trap 'cleanup' EXIT
trap 'cleanup' INT
trap 'cleanup' TERM

# Right — use valid signal numbers
trap 'echo "HUP received"' 1
trap 'echo "INT received"' 2
trap 'echo "TERM received"' 15

# List all available signals
trap -l 
```

### Solution 2: Use EXIT for Cleanup Instead of Specific Signals

The `EXIT` pseudo-signal runs when the script exits for any reason, making it ideal for cleanup tasks. It avoids the need to trap multiple signals.

```bash
#!/bin/bash

# EXIT trap runs on any exit — no need for multiple signal traps
cleanup() {
    rm -f /tmp/myapp_*
    echo "Cleanup complete"
}
trap cleanup EXIT

# You can also trap specific signals alongside EXIT
trap 'echo "Interrupted!"; exit 1' INT TERM

# Simpler approach — just use EXIT
trap 'rm -f /tmp/lockfile' EXIT

# Remove the trap
trap - EXIT 
```

## Prevention Tips

- Use `trap -l` to list all available signals on your system
- Use `EXIT` pseudo-signal for cleanup code — it covers all exit paths
- Use signal names without the `SIG` prefix (e.g., `INT`, not `SIGINT`)

## Related Errors

- [Broken Pipe]({< relref "/languages/bash/broken-pipe-error" >})
- [Job Control Error]({< relref "/languages/bash/job-control-error" >})
