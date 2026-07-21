---
title: "Julia InterruptException Async Task Error"
description: "Fix Julia InterruptException errors when async tasks are interrupted unexpectedly during execution."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`InterruptException` is thrown when Ctrl+C or an interrupt signal is received during computation. In async contexts, this can cause tasks to fail unpredictably.

## Common Causes

- User presses Ctrl+C during long computation
- Task scheduler interrupts long-running task
- Signal handler not properly configured
- Async tasks not protected from interrupts
- Interrupt during critical section leaves inconsistent state

## How to Fix

```julia
# WRONG: Long computation without interrupt handling
function long_computation()
    for i in 1:10^9
        sqrt(i)  # InterruptException possible
    end
end

# CORRECT: Use try-catch for interrupts
function long_computation()
    try
        for i in 1:10^9
            sqrt(i)
        end
    catch e
        if e isa InterruptException
            println("Computation interrupted at step")
        else
            rethrow(e)
        end
    end
end
```

```julia
# WRONG: Async task without protection
@async begin
    # this task can be interrupted
    heavy_computation()
end

# CORRECT: Shield critical tasks
t = Threads.@spawn begin
    try
        heavy_computation()
    catch e
        e isa InterruptException || rethrow(e)
    end
end
```

## Examples

```julia
# Example 1: Safe computation with cleanup
function safe_computation(data)
    result = nothing
    try
        result = complex_process(data)
    catch e
        e isa InterruptException && cleanup()
        rethrow(e)
    end
    return result
end

# Example 2: Async with timeout
function with_timeout(f, timeout_sec)
    task = @async f()
    timer = Timer(timeout_sec)
    while !istaskdone(task)
        if !isopen(timer)
            schedule(task, InterruptException(), error=true)
            return nothing
        end
        sleep(0.01)
    end
    return fetch(task)
end

# Example 3: Multiple async tasks
tasks = [@async process(i) for i in 1:10]
results = [fetch(t) for t in tasks if istaskdone(t)]
```

## Related Errors

- [Task error](julia-task-error) -- async task failures
- [System error](julia-system-error) -- OS-level errors
