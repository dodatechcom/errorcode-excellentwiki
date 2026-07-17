---
title: "[Solution] Ruby RangeError — Number Out of Range Fix"
description: "Fix Ruby RangeError: X out of range. Handle integer overflow, Float::INFINITY, and range boundaries."
languages: ["ruby"]
severities: ["error"]
error_types: ["range"]
weight: 100
---

# RangeError — Number Out of Range Fix

A `RangeError` is raised when a numeric operation produces a result outside the representable range, or when an invalid range is created.

## Description

Ruby has fixed-size integer types (`Fixnum`/`Bignum` unified as `Integer`) and float limits. Operations that exceed these limits raise `RangeError`.

Common scenarios:

- **Integer too large for conversion** — converting a huge number to a smaller type.
- **Invalid range boundaries** — creating an invalid range with `exclude_end?`.
- **Float conversion overflow** — converting `Float::INFINITY` to `Integer`.
- **Begin greater than end with exclude_end?** — `(5...3)` raises RangeError.

## Common Causes

```ruby
# Cause 1: Converting out-of-range Float to Integer
Float::INFINITY.to_i  # RangeError: Infinity

# Cause 2: Invalid range with exclude_end?
(5...3).to_a  # RangeError: 3 is out of range for exclude_end?

# Cause 3: Huge number conversion edge cases
(10**100).to_i  # Works (Ruby handles big integers)
(10**100).to_f  # Works (becomes Infinity)

# Cause 4: Converting NaN to Integer
Float::NAN.to_i  # FloatDomainError (related error)
```

## Solutions

### Fix 1: Validate before conversion

```ruby
# Wrong
def convert_to_int(value)
  value.to_i
end

# Correct
def convert_to_int(value)
  return nil if value.is_a?(Float) && value.infinite?
  return nil if value.is_a?(Float) && value.nan?
  value.to_i
end
```

### Fix 2: Handle infinity explicitly

```ruby
# Wrong
Float::INFINITY.to_i  # RangeError

# Correct
value = Float::INFINITY
result = value.finite? ? value.to_i : nil
```

### Fix 3: Create valid ranges

```ruby
# Wrong — RangeError with exclude_end?
(5...3).to_a

# Correct — use inclusive range or swap endpoints
(3..5).to_a      # [3, 4, 5]
(5..3).to_a      # [] (empty, but valid)
5.downto(3).to_a # [5, 4, 3]
```

### Fix 4: Use BigDecimal for large numbers

```ruby
require 'bigdecimal'

# Wrong — Float loses precision
big = 1e308 * 10  # Infinity

# Correct — BigDecimal maintains precision
big = BigDecimal("1e308") * 10  # Works with full precision
```

## Related Errors

- [FloatDomainError](float-domain-error) — NaN or Infinity in domain-specific operations.
- [ZeroDivisionError](zero-division-error) — division by zero.
- [ArgumentError](argument-error) — wrong number of arguments.
