---
title: "Julia AssertionError Failed Assert Macro"
description: "Fix Julia AssertionError when assert macros fail due to false conditions in development code."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`AssertionError` is thrown when an `@assert` macro condition evaluates to false. Assertions are used for debugging and should catch impossible states during development.

## Common Causes

- Input validation logic is incorrect
- Assertion condition has logical error
- Using @assert for input validation (should use throw)
- Assertion disabled with --check-bounds=no but expected
- Floating point comparison in assertion fails due to precision

## How to Fix

```julia
# WRONG: Using @assert for user input
function divide(a, b)
    @assert b != 0  # AssertionError not appropriate
    a / b
end

# CORRECT: Use explicit error throwing
function divide(a, b)
    b == 0 && throw(ArgumentError("division by zero"))
    a / b
end
```

```julia
# WRONG: Floating point comparison in assert
x = 0.1 + 0.2
@assert x == 0.3  # fails due to floating point

# CORRECT: Use approximate comparison
@assert x ≈ 0.3  # isapprox(x, 0.3)
```

## Examples

```julia
# Example 1: Debug assertions
function process(data::Vector{Int})
    @assert length(data) > 0 "data must not be empty"
    @assert all(x -> x > 0, data) "all elements must be positive"
    sum(data)
end

# Example 2: Custom assertion macro
macro my_assert(cond, msg)
    :(if !$(esc(cond))
        error("Assertion failed: " * $(esc(msg)))
    end)
end

# Example 3: Test assertions
@testset "basic tests" begin
    @test 1 + 1 == 2
    @test_throws ArgumentError divide(1, 0)
end
```

## Related Errors

- [Assertion error](julia-assertion-error-fix) -- assertion failures
- [ArgumentError](julia-argument-error) -- invalid arguments
