---
title: "Julia Workspace Variable Capture Error"
description: "Fix Julia workspace variable capture errors when closures capture variables by reference instead of value."
languages: ["julia"]
error-types: ["logic-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Variable capture errors occur when closures capture variables by reference, so the closure sees the latest value of the variable rather than the value at creation time. This causes unexpected behavior in loops and callbacks.

## Common Causes

- Closure captures loop variable by reference
- Multiple closures share same captured variable
- Variable modified after closure creation
- Global variable captured instead of local
- Intentional value capture requires special syntax

## How to Fix

```julia
# WRONG: Loop variable captured by reference
funcs = []
for i in 1:5
    push!(funcs, () -> i)
end
[f() for f in funcs]  # [5, 5, 5, 5, 5] not [1, 2, 3, 4, 5]

# CORRECT: Capture by value
funcs = []
for i in 1:5
    push!(funcs, (i -> () -> i)(i))
end
[f() for f in funcs]  # [1, 2, 3, 4, 5]
```

```julia
# WRONG: Shared mutable state
counter = 0
funcs = []
for _ in 1:5
    push!(funcs, () -> (global counter += 1))
end
[f() for f in funcs]  # all see same counter

# CORRECT: Use local copy
funcs = []
for _ in 1:5
    local c = 0
    push!(funcs, () -> (c += 1))
end
```

## Examples

```julia
# Example 1: Classic loop capture problem
f1, f2, f3 = begin
    fs = []
    for i in 1:3
        push!(fs, () -> i)
    end
    fs
end
# All return 3 -- all capture same i

# Fix with let block
f1, f2, f3 = begin
    fs = []
    for i in 1:3
        let i = i  # create new local binding
            push!(fs, () -> i)
        end
    end
    fs
end
# Returns 1, 2, 3

# Example 2: Callback pattern
function create_callbacks()
    callbacks = []
    for name in ["Alice", "Bob", "Charlie"]
        let name = name
            push!(callbacks, () -> println("Hello, $name"))
        end
    end
    return callbacks
end

# Example 3: Timer with correct capture
timers = []
for delay in [0.1, 0.2, 0.3]
    let delay = delay
        t = Timer(_) -> println("Timer: $delay") do
            # fires after delay
        end
        push!(timers, t)
    end
end
```

## Related Errors

- [Closure error](julia-closure-error) -- closure-related issues
- [Task error](julia-task-error) -- async task issues
