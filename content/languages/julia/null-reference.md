---
title: "NullReferenceException"
description: "A NullReferenceException occurs when attempting to access a method or property on a null or missing value."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["null", "reference", "nothing", "exception"]
weight: 5
---

## What This Error Means

In Julia, `Nothing` is used to represent the absence of a value. A `NullReferenceException`-like error occurs when you try to call a function or access a field on `nothing`. While Julia doesn't have a literal `NullReferenceException` like C#, the equivalent error occurs when operations are attempted on `nothing`.

## Common Causes

- Function returns `nothing` instead of an expected value
- Uninitialized optional fields
- Missing data from database or API calls
- Pattern matching that doesn't handle `nothing` case

## How to Fix

```julia
# WRONG: Calling method on nothing
function find_value(dict, key)
    # returns nothing if key missing
end
result = find_value(mydict, "key")
println(result.length)  # Error: method not defined for Nothing

# CORRECT: Check for nothing first
result = find_value(mydict, "key")
if result !== nothing
    println(length(result))
end
```

```julia
# WRONG: Not handling nothing return
value = parse(Int, "abc")  # returns nothing on failure
 doubled = value * 2       # Error

# CORRECT: Use try-catch or validate
try
    value = parse(Int, "abc")
    doubled = value * 2
catch e
    println("Parse failed: ", e)
end
```

## Examples

```julia
# Example 1: Nothing from function
function safe_get(arr, idx)
    idx <= length(arr) ? arr[idx] : nothing
end
val = safe_get([1, 2, 3], 10)
println(val + 1)  # Error: method not defined for Nothing

# Example 2: Missing dictionary key
d = Dict("a" => 1)
v = get(d, "b", nothing)
println(v * 2)    # Error on nothing

# Example 3: Nullable pattern
x = nothing
y = x.field      # Error: type Nothing has no field
```

## Related Errors

- [UndefVarError: X not defined](/languages/julia/undefined-sym)
- [BoundsError: attempt to access X at index [Y]](/languages/julia/bounds-error)
