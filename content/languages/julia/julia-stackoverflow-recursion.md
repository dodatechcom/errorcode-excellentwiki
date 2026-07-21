---
title: "Julia StackOverflowError in Deep Recursion"
description: "Fix Julia StackOverflowError when recursive functions exceed the default stack depth limit."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`StackOverflowError` occurs when function calls recurse too deeply, exhausting the JVM/Julia call stack. The default stack size limits recursion depth.

## Common Causes

- Recursive function without proper base case
- Base case is unreachable due to logic error
- Mutual recursion creating deep call chains
- Large data structures causing deep recursive traversal
- Missing tail-call optimization in recursive patterns

## How to Fix

```julia
# WRONG: Base case never reached
function factorial(n)
    return n * factorial(n - 1)  # StackOverflowError at n=0
end

# CORRECT: Proper base case
function factorial(n)
    n <= 1 ? 1 : n * factorial(n - 1)
end
factorial(20)  # 2432902008176640000
```

```julia
# WRONG: Deep recursion on list
function sum_list(lst)
    isempty(lst) ? 0 : first(lst) + sum_list(rest(lst))
end
sum_list(1:100000)  # StackOverflowError

# CORRECT: Use iteration or built-in sum
sum(1:100000)  # 5000050000
```

## Examples

```julia
# Example 1: Fibonacci with memoization
function fib_memo(n, memo=Dict{Int,Int}())
    haskey(memo, n) && return memo[n]
    result = n <= 2 ? n : fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result
end
fib_memo(100)  # works without stack overflow

# Example 2: Tree traversal
mutable struct TreeNode
    value::Int
    children::Vector{TreeNode}
end

function depth(node::TreeNode)
    isempty(node.children) ? 0 : 1 + maximum(depth(c) for c in node.children)
end

# Example 3: Increase stack size
task = Task(() -> deep_recursion())
schedule(task)
wait(task)
```

## Related Errors

- [BoundsError](bounds-error) -- index out of bounds
- [MethodError](julia-method-error) -- method not found
