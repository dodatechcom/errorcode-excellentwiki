---
title: "CompositeException in Julia"
description: "Julia raises CompositeException when multiple errors occur in parallel tasks or async operations"
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `CompositeException` is thrown when multiple errors occur simultaneously in parallel tasks or asynchronous operations. It wraps multiple individual exceptions into a single composite error.

## Common Causes

- Multiple parallel tasks fail simultaneously
- @sync block with multiple failing tasks
- Distributed computing errors across workers
- Channel operations with multiple producers failing

## How to Fix

Handle individual task errors:

```julia
tasks = map(1:5) do i
    @async begin
        if i == 3
            error("Task $i failed")
        end
        i * 2
    end
end

try
    results = fetch.(tasks)
catch e
    if e isa CompositeException
        for (i, ex) in enumerate(e.exceptions)
            println("Exception $i: $(ex)")
        end
    end
end
```

Use `@sync` with error handling:

```julia
@sync begin
    @async process_data()
    @async process_other()
end
# If both fail, CompositeException is thrown
```

Handle distributed errors:

```julia
using Distributed
addprocs(4)

@everywhere function risky_computation(x)
    x > 100 && error("Value too large: $x")
    x^2
end

try
    results = pmap(risky_computation, 1:200)
catch e
    if e isa CompositeException
        println("$(length(e.exceptions)) tasks failed")
    end
end
```

Use `errormonitor` for background tasks:

```julia
t = @async begin
    error("Background task failed")
end
errormonitor(t)  # Logs error without blocking
```

## Examples

```julia
@sync begin
    @async error("First error")
    @async error("Second error")
end
# CompositeException with 2 exceptions
```

## Related Errors

- [ArgumentError]({{< relref "/languages/julia/argumenterror" >}})
- [BoundsError]({{< relref "/languages/julia/bounds-error" >}})
