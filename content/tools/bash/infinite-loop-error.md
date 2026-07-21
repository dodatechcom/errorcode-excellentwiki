---
title: "[Solution] Bash Infinite Loop Error"
description: "Fix Bash infinite loop errors when while or for loops run indefinitely without exit conditions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Infinite Loop Error

Bash loops run forever because the exit condition is never met.

```
^C  # Ctrl+C required to stop
```

## Common Causes

- Loop variable not updated inside loop
- Exit condition logic inverted
- read command blocking on stdin
- Counter not incrementing
- File being watched never changes

## How to Fix

### Add Timeout Safety

```bash
#!/bin/bash
SECONDS=0
TIMEOUT=300

while true; do
    if (( SECONDS > TIMEOUT )); then
        echo "Timed out after ${TIMEOUT}s" >&2
        break
    fi
    # Check condition
    if check_condition; then
        break
    fi
    sleep 1
done
```

### Ensure Loop Variable Updates

```bash
# Broken - i never increments
i=0
while [[ $i -lt 10 ]]; do
    echo "$i"
done

# Fixed
i=0
while [[ $i -lt 10 ]]; do
    echo "$i"
    ((i++))
done
```

### Use timeout Command

```bash
# Kill script after 60 seconds
timeout 60 bash -c '
    while true; do
        check_condition && break
        sleep 5
    done
'
```

### Add Break on Empty Input

```bash
while read -r line; do
    [[ -z "$line" ]] && continue
    process "$line"
done < input.txt
```

## Examples

```bash
# Monitor file with timeout
#!/bin/bash
start_time=$SECONDS
while true; do
    if grep -q "ready" /var/log/app.log 2>/dev/null; then
        echo "Service ready"
        break
    fi
    if (( SECONDS - start_time > 120 )); then
        echo "Timeout waiting for service" >&2
        exit 1
    fi
    sleep 2
done
```
