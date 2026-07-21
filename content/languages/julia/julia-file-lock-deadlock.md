---
title: "Julia File Lock Deadlock Error"
description: "Fix Julia file lock errors when multiple processes or tasks deadlock waiting for file locks."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

File lock deadlocks occur when multiple processes or async tasks wait for file locks held by each other, or when a lock is acquired but never released due to error paths.

## Common Causes

- Lock acquired but not released in error path
- Multiple locks acquired in inconsistent order
- Lock file left behind after process crash
- File descriptor leak preventing lock release
- Blocking lock without timeout

## How to Fix

```julia
# WRONG: Lock not released on error
function process_file(path)
    lock = FileLock(path * ".lock")
    acquire(lock)
    # if error occurs here, lock is never released!
    data = read(path, String)
    write(path * ".processed", data)
    release(lock)
end

# CORRECT: Use try-finally
function process_file(path)
    lock = FileLock(path * ".lock")
    acquire(lock)
    try
        data = read(path, String)
        write(path * ".processed", data)
    finally
        release(lock)
    end
end
```

```julia
# WRONG: Deadlock between two files
@async begin
    acquire(lock_a)  # holds lock_a
    sleep(0.1)
    acquire(lock_b)  # waits for lock_b
end

@async begin
    acquire(lock_b)  # holds lock_b
    sleep(0.1)
    acquire(lock_a)  # waits for lock_a -- DEADLOCK
end

# CORRECT: Acquire locks in consistent order
# Always acquire lock_a before lock_b
```

## Examples

```julia
# Example 1: Safe file locking
using FileWatching

function safe_write(path, content)
    lock_path = path * ".lock"
    open(lock_path, "w") do f
        lock(f) do
            write(path, content)
        end
    end
end

# Example 2: Process-safe locking
function process_safe(path)
    mktemp() do tmp, io
        write(io, read(path))
        flush(io)
        mv(tmp, path; force=true)
    end
end

# Example 3: Try-lock with timeout
function try_lock_with_timeout(lock, timeout=5.0)
    start = time()
    while !trylock(lock)
        if time() - start > timeout
            error("Could not acquire lock")
        end
        sleep(0.01)
    end
    return true
end
```

## Related Errors

- [Deadlock error](julia-deadlock-error) -- general deadlocks
- [File IO error](julia-io-stream-error) -- file operation issues
