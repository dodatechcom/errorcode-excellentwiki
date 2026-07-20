---
title: "[Solution] Parallel Execution Error in Bash"
description: "Fix parallel command execution errors in Bash pipelines."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Parallel Execution Error in Bash

Commands run in parallel have race conditions or resource conflicts.

### Common Causes
- Multiple background jobs writing to the same file.
- Shared resource access without locking.
- Too many parallel processes consuming memory.

### How to Fix
```bash
# Use file locking
(
    flock -n 200 || { echo "Locked" >&2; exit 1; }
    echo "data" >> shared_file
) 200>"$lockfile"

# Limit parallelism
for i in $(seq 1 100); do
    process "$i" &
    (( $(jobs -r | wc -l) >= $(nproc) )) && wait -n
done
wait

# Use GNU parallel for robust parallelism
parallel -j 4 process ::: {1..100}
```

### Example
```bash
# Broken (race condition)
for i in {1..100}; do
    echo "$i" >> output.txt &
done

# Fixed
for i in {1..100}; do
    echo "$i" >> output.txt &
done
wait
```
