---
title: "Julia Printf Format String Error"
description: "Fix Julia @printf and @sprintf format string errors when format specifiers do not match argument types."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`@printf` and `@sprintf` format errors occur when format specifiers like `%d`, `%f`, `%s` do not match the actual argument types, or when format strings have syntax errors.

## Common Causes

- Using %d for floating point numbers
- Wrong number of arguments for format string
- Format specifier not supported (e.g., %u for unsigned)
- Escape sequences incorrectly formatted
- Missing @printf macro import from Printf

## How to Fix

```julia
# WRONG: Format specifier mismatch
using Printf
@printf("%d", 3.14)  # %d is for integers

# CORRECT: Match specifier to type
@printf("%f", 3.14)  # 3.140000
```

```julia
# WRONG: Missing import
@printf("%d", 42)  # UndefVarError: @printf not defined

# CORRECT: Import Printf module
using Printf
@printf("%d", 42)  # 42
```

## Examples

```julia
# Example 1: Basic formatting
using Printf
@printf("Integer: %d\n", 42)
@printf("Float: %.2f\n", 3.14159)
@printf("String: %s\n", "hello")

# Example 2: Formatted output
x = 1234.5678
@printf("Formatted: %10.2f\n", x)   # "   1234.57"
@printf("Padded: %010d\n", 42)      # "0000000042"

# Example 3: String formatting
s = @sprintf("Pi is approximately %.4f", π)
println(s)  # "Pi is approximately 3.1416"
```

## Related Errors

- [IO error](julia-io-stream-error) -- I/O operation issues
- [ArgumentError](julia-argument-error) -- invalid arguments
