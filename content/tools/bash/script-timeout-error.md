---
title: "[Solution] Bash Script Timeout Error"
description: "Fix Bash script timeout errors when scripts hang or exceed execution time limits."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Script Timeout Error

Bash scripts hang or run longer than expected, triggering timeout mechanisms.

```
Command timed out after 300 seconds
```

## Common Causes

- Script stuck in infinite loop
- Network command hanging without timeout
- Waiting on user input in non-interactive context
- Child process not terminating
- Deadlock in background processes

## How to Fix

### Use timeout Command

```bash
# Kill command after 60 seconds
timeout 60 curl http://example.com

# With custom exit code on timeout
timeout --signal=KILL 30 ./long_script.sh
echo "Exit code: $?"
```

### Add Internal Timeout

```bash
#!/bin/bash
SECONDS=0
TIMEOUT=120

while true; do
    if (( SECONDS > TIMEOUT )); then
        echo "Script timed out after ${TIMEOUT}s" >&2
        kill -- -$$ 2>/dev/null
        exit 124
    fi
    # Do work
    sleep 1
done
```

### Set Timeouts on Commands

```bash
# Network command with timeout
curl --max-time 10 http://example.com

# SSH connection timeout
ssh -o ConnectTimeout=5 user@host

# DNS lookup timeout
timeout 5 nslookup example.com
```

### Kill Stuck Child Processes

```bash
#!/bin/bash
cleanup() {
    kill 0 2>/dev/null
}
trap cleanup EXIT

timeout 30 bash -c '
    long_running_task &
    wait
'
```

### Use set -T for Job Control

```bash
#!/bin/bash
set -m  # Enable job control

# Now fg and bg work
sleep 100 &
PID=$!
sleep 2
kill "$PID" 2>/dev/null
```

## Examples

```bash
#!/bin/bash
# Script with multiple timeout levels

TIMEOUT=${1:-300}
SCRIPT_PID=$$

# External watchdog
(
    sleep "$TIMEOUT"
    kill -TERM "$SCRIPT_PID" 2>/dev/null
) &
WATCHDOG_PID=$!

# Main work
main() {
    echo "Starting work..."
    sleep 5
    echo "Work complete"
}

trap 'kill $WATCHDOG_PID 2>/dev/null' EXIT
main
```
