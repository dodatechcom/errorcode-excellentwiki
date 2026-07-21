---
title: "Julia Distributed Worker Process Crash Error"
description: "Fix Julia Distributed worker process crashes when worker processes die unexpectedly during parallel computation."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Worker process crashes in Julia's Distributed module cause `ProcessExitedException` or `CompositeException` when the main process tries to communicate with a dead worker.

## Common Causes

- Worker runs out of memory (OOM killer)
- Segfault in native code on worker
- Excessive garbage collection pauses on worker
- Worker has infinite loop consuming all resources
- Network disconnection between workers

## How to Fix

```julia
# WRONG: Not handling worker failure
using Distributed
addprocs(4)
results = pmap(process, large_data)  # crashes if worker dies

# CORRECT: Handle worker failures gracefully
using Distributed
addprocs(4)
results = try
    pmap(process, large_data)
catch e
    if e isa ProcessExitedException
        println("A worker crashed")
        # retry or fallback
    end
    rethrow(e)
end
```

```julia
# WRONG: Worker not checked before use
workers()  # may be empty after crash

# CORRECT: Verify workers are alive
function safe_workers()
    alive = filter(w -> w > 0 && isalive(w), workers())
    if isempty(alive)
        addprocs(4)
        return workers()
    end
    return alive
end
```

## Examples

```julia
# Example 1: Check worker health
using Distributed
addprocs(4)

@everywhere function heavy_computation(n)
    # potential crash point
    rand(n, n) * rand(n, n)
end

try
    results = pmap(heavy_computation, [100, 200, 300])
catch e
    println("Worker error: ", e)
    rmprocs(workers())
    addprocs(4)
end

# Example 2: Monitor workers
function check_workers()
    for w in workers()
        try
            remotecall_fetch(() -> myid(), w)
        catch
            println("Worker $w is dead")
        end
    end
end
```

## Related Errors

- [Process failed error](julia-process-failed) -- process failures
- [Distributed error](julia-distributed-error) -- distributed computing issues
