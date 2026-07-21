---
title: "[Solution] Bash Wait Error -- Process Synchronization Issues"
description: "Fix bash wait errors when using wait command for process synchronization incorrectly."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Wait Error

This error occurs when `wait` is used incorrectly, such as waiting on non-existent PIDs.

## Common Causes

- Waiting on a PID that has already exited
- Not capturing PID before background process starts
- Using `wait` without arguments in scripts (waits for all)
- Multiple background jobs with incorrect PID tracking

## How to Fix

### Capture PID before waiting

```bash
# WRONG: PID may be wrong
./long_task &
wait $!  # works but fragile

# CORRECT: store and check PID
./long_task &
pid=$!
wait $pid
exit_code=$?
```

### Wait for all background jobs

```bash
# Start multiple jobs
for i in {1..5}; do
    process_item "$i" &
done

# Wait for all and collect exit codes
fail=0
for pid in $(jobs -p); do
    wait "$pid" || fail=$((fail + 1))
done
echo "Failed: $fail"
```

## Examples

```bash
#!/bin/bash
task1 &
pid1=$!
task2 &
pid2=$!

wait $pid1 && echo "Task 1 done" || echo "Task 1 failed"
wait $pid2 && echo "Task 2 done" || echo "Task 2 failed"
```
