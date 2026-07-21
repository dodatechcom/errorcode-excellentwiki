---
title: "[Solution] Bash Background Job Error"
description: "Fix Bash background job errors when bg, fg, or job control commands fail."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Background Job Error

Bash background job control commands fail or behave unexpectedly.

```
bash: bg: no such job
bash: fg: no such job
```

## Common Causes

- Job already completed before bg/fg
- Running in non-interactive shell (no job control)
- Job PID no longer valid
- Job control not enabled (set +m)
- Script runs in subshell

## How to Fix

### Enable Job Control

```bash
# Enable job control in script
set -m

# Start background job
sleep 100 &
JOB_PID=$!
echo "Job started: $JOB_PID"
```

### Track Background Jobs

```bash
#!/bin/bash
set -m

# Start background tasks
task1 &
PID1=$!

task2 &
PID2=$!

# Wait for all background jobs
for pid in $PID1 $PID2; do
    if wait "$pid"; then
        echo "Job $pid completed successfully"
    else
        echo "Job $pid failed with code $?" >&2
    fi
done
```

### Use disown to Detach Jobs

```bash
# Detach job from shell so it survives shell exit
long_running_task &
disown

# Or use nohup
nohup long_running_task > output.log 2>&1 &
```

### Handle Non-Interactive Shells

```bash
#!/bin/bash
# Job control works differently in non-interactive mode

# Use PID tracking instead of job IDs
background_cmd &
BGPID=$!

# Check if background process is running
if kill -0 "$BGPID" 2>/dev/null; then
    echo "Background job running"
fi

# Wait with timeout
if ! timeout 10 wait "$BGPID" 2>/dev/null; then
    echo "Background job timed out"
    kill "$BGPID" 2>/dev/null
fi
```

### List Active Jobs

```bash
# List all jobs
jobs -l

# List only running jobs
jobs -r

# List only stopped jobs
jobs -s
```

## Examples

```bash
#!/bin/bash
set -m

# Run multiple jobs in parallel
for server in web1 web2 web3; do
    ssh "$server" "uptime" &
done

# Wait for all jobs
wait
echo "All servers checked"
```
