---
title: "Julia Enum Value Out Of Range Error"
description: "Fix Julia @enum errors when using enum values outside the defined range or converting between enum and integer incorrectly."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Enum errors occur when you try to create an enum value from an integer that is not in the defined set, or when performing operations not supported on enum types.

## Common Causes

- Integer-to-enum conversion with out-of-range value
- Using enum in arithmetic operations
- Comparing enum to wrong type
- Missing enum value in switch/match
- Enum values not starting from expected value

## How to Fix

```julia
# WRONG: Out of range integer to enum
@enum Color RED=1 GREEN=2 BLUE=3
Color(4)  # ArgumentError: invalid value for enum Color: 4

# CORRECT: Check range first
function safe_color(v::Int)
    v in 1:3 ? Color(v) : error("Invalid color value: $v")
end
```

```julia
# WRONG: Arithmetic on enums
@enum Direction NORTH=1 SOUTH=2 EAST=3 WEST=4
result = NORTH + SOUTH  # MethodError

# CORRECT: Convert to integer first
result = Int(NORTH) + Int(SOUTH)  # 3
```

## Examples

```julia
# Example 1: Define and use enums
@enum Planet MERCURY=1 VENUS=2 EARTH=3 MARS=4
p = EARTH
println(p)  # EARTH
println(Int(p))  # 3

# Example 2: Enum in conditional
function describe(p::Planet)
    p == EARTH ? "Our home" :
    p == MARS ? "Red planet" :
    "Unknown"
end

# Example 3: Enum array
planets = [MERCURY, VENUS, EARTH, MARS]
for p in planets
    println("$p is planet number $(Int(p))")
end
```

## Related Errors

- [ArgumentError](julia-argument-error) -- invalid arguments
- [InexactError](julia-inexact-error) -- type conversion failure
