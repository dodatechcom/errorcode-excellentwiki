---
title: "[Solution] Ruby FloatDomainError — NaN Fix"
description: "Fix Ruby FloatDomainError: NaN. Handle NaN and Infinity values in mathematical operations and comparisons."
languages: ["ruby"]
severities: ["error"]
error_types: ["float-domain"]
weight: 110
---

# FloatDomainError — NaN Fix

A `FloatDomainError` is raised when you try to convert `Float::NAN` or `Float::INFINITY` to an integer, or use them in operations that require finite values.

## Description

Ruby has special float values: `Float::NAN` (Not a Number) and `Float::INFINITY`. These values can't be meaningfully converted to integers or used in certain comparisons. Attempting to do so raises `FloatDomainError`.

Common scenarios:

- **Converting NaN to Integer** — `Float::NAN.to_i` raises `FloatDomainError`.
- **NaN comparisons** — `Float::NAN == Float::NAN` returns `false`.
- **Math operations producing NaN** — `Math.sqrt(-1)` returns `NaN`.
- **Invalid operations** — `0.0 / 0.0` returns `NaN`.

## Common Causes

```ruby
# Cause 1: Converting NaN to Integer
Float::NAN.to_i  # FloatDomainError: NaN

# Cause 2: NaN from math operations
result = Math.sqrt(-1)  # NaN
result.to_i  # FloatDomainError

# Cause 3: NaN from invalid operations
0.0 / 0.0  # NaN
result = 0.0 / 0.0
result.to_i  # FloatDomainError

# Cause 4: NaN in comparisons
Float::NAN == Float::NAN  # false (always!)
Float::NAN.eql?(Float::NAN)  # false
```

## Solutions

### Fix 1: Check for NaN before conversion

```ruby
# Wrong
def safe_to_i(value)
  value.to_i
end

# Correct
def safe_to_i(value)
  return nil if value.nan?
  return nil if value.infinite?
  value.to_i
end
```

### Fix 2: Use Float::NAN? to check

```ruby
result = Math.sqrt(-1)  # NaN

# Wrong
puts result.to_i  # FloatDomainError

# Correct
if result.nan?
  puts "Result is not a valid number"
else
  puts result.to_i
end
```

### Fix 3: Handle NaN in comparisons

```ruby
# Wrong
value = Float::NAN
if value == Float::NAN  # Always false!
  puts "It's NaN"
end

# Correct
if value.nan?
  puts "It's NaN"
end
```

### Fix 4: Use BigDecimal for precise math

```ruby
require 'bigdecimal'

a = BigDecimal("0")
b = BigDecimal("0")
result = a / b  # Infinity (BigDecimal)

if result.infinite?
  puts "Result is infinite"
elsif result.nan?
  puts "Result is NaN"
else
  puts result.to_i
end
```

## Related Errors

- [RangeError](range-error) — number too large for range.
- [ZeroDivisionError](zero-division-error) — division by zero.
- [Math::DomainError](math-domain-error) — math function domain error.
