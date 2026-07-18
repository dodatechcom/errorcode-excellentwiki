---
title: "[Solution] Fix StackOverflowError recursion depth exceeded in Julia"
description: "Resolve StackOverflowError in Julia by converting deep recursion to iteration, using the @tailcall macro for tail calls, and applying memoization caching."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

A `StackOverflowError` is thrown when the call stack exceeds its maximum depth due to too many recursive function calls. Julia has a limited stack size (typically around 8MB on Linux), and deep recursion fills it quickly.

The error appears as:

```julia
StackOverflowError:
```

with a long stack trace showing the same function called repeatedly.

## Why It Happens

This error occurs due to unbounded recursion:

- Recursive function without a proper base case
- Base case is never reached due to logic error
- Recursion depth grows too fast (e.g., exponential branching)
- Mutual recursion between two or more functions without limits
- Accidentally calling a function within itself through a different name

## How to Fix It

Convert recursion to iteration:

```julia
# WRONG: Recursive factorial (stack overflow for large n)
function factorial(n)
    n <= 1 ? 1 : n * factorial(n - 1)
end

# CORRECT: Iterative version
function factorial_iter(n)
    result = 1
    for i in 2:n
        result *= i
    end
    return result
end

factorial_iter(100000)  # Works
```

Use `@tailcall` macro for tail-recursive functions (Julia 1.9+):

```julia
function factorial_tail(n, acc=1)
    @tailcall n <= 1 ? acc : factorial_tail(n - 1, acc * n)
end

factorial_tail(100000)  # Optimized with tail-call elimination
```

Use memoization to avoid redundant recursive calls:

```julia
using Memoize

@memoize function fibonacci(n)
    n <= 2 ? 1 : fibonacci(n-1) + fibonacci(n-2)
end

fibonacci(100)  # Fast with memoization
```

Use an explicit stack for tree traversal:

```julia
# WRONG: Recursive tree traversal
function traverse(node)
    process(node)
    for child in node.children
        traverse(child)
    end
end

# CORRECT: Iterative with explicit stack
function traverse_iter(root)
    stack = [root]
    while !isempty(stack)
        node = pop!(stack)
        process(node)
        append!(stack, node.children)
    end
end
```

Increase stack size as a temporary fix:

```bash
# Linux
ulimit -s unlimited
julia my_script.jl
```

## Common Mistakes

- Writing recursive solutions without a clear base case
- Not realizing that Julia does not guarantee tail-call optimization
- Using recursion for problems that are naturally iterative
- Not using memoization for overlapping subproblems
- Forgetting that mutual recursion also consumes stack space

## Related Pages

- [MethodError: no method matching](/languages/julia/julia-method-error)
- [BoundsError: array index out of bounds](/languages/julia/bounds-error)
- [UndefVarError: function not defined](/languages/julia/julia-undefined-function)
