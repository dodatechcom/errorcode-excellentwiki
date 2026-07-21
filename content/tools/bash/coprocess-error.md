---
title: "[Solution] Bash Coprocess Error"
description: "Fix Bash coprocess errors when background coprocess communication fails or becomes unresponsive."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Coprocess Error

Bash coprocess communication fails or the coprocess becomes unresponsive.

```
bash: write error: Broken pipe
```

## Common Causes

- Coprocess process terminated unexpectedly
- Pipe buffer full due to slow reader
- Coprocess not reading from stdin
- File descriptor leak
- Coprocess defined in subshell and lost

## How to Fix

### Proper Coprocess Definition

```bash
# Define coprocess at the same shell level
coproc MY_COPROC { cat; }
echo "Hello" >&"${MY_COPROC[1]}"
read -r line <&"${MY_COPROC[0]}"
echo "$line"
```

### Handle Broken Pipe

```bash
# Check if coprocess is still alive
if kill -0 "${MY_COPROC_PID}" 2>/dev/null; then
    echo "data" >&"${MY_COPROC[1]}"
else
    echo "Coprocess died, restarting..."
    coproc MY_COPROC { cat; }
fi
```

### Use Timeout for Reads

```bash
coproc MY_COPROC { sleep 10; echo "output"; }

# Read with timeout
if read -t 5 -r line <&"${MY_COPROC[0]}"; then
    echo "Got: $line"
else
    echo "Read timed out"
    kill "${MY_COPROC_PID}" 2>/dev/null
fi
```

### Clean Up Coprocess

```bash
coproc MY_COPROC { some_command; }

# Always clean up on exit
trap 'kill "${MY_COPROC_PID}" 2>/dev/null' EXIT
```

## Examples

```bash
# Coprocess for parallel processing
coproc WORKER { while read -r cmd; do eval "$cmd"; done; }

echo "ls -la" >&"${WORKER[1]}"
read -r result <&"${WORKER[0]}"
echo "$result"

# Signal completion
echo "exit" >&"${WORKER[1]}"
wait "${WORKER_PID}"
```
