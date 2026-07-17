---
title: "[Solution] Ruby Math::DomainError — Math Domain Error Fix"
description: "Fix Ruby Math::DomainError. Handle invalid mathematical operations like Math.sqrt(-1) or Math.log(-1)."
languages: ["ruby"]
severities: ["error"]
error_types: ["math-domain"]
weight: 130
---

# Math::DomainError — Math Domain Error Fix

A `Math::DomainError` is raised when a mathematical function receives an argument outside its valid domain.

## Description

Many math functions have domain restrictions. For example, `Math.sqrt` only works with non-negative numbers, and `Math.log` only works with positive numbers. Passing invalid arguments raises `Math::DomainError`.

Common scenarios:

- **Negative square root** — `Math.sqrt(-1)`.
- **Negative logarithm** — `Math.log(-1)`.
- **Log of zero** — `Math.log(0)`.
- **Asin/Acos out of range** — `Math.asin(2)` (must be -1 to 1).

## Common Causes

```ruby
# Cause 1: Negative square root
Math.sqrt(-1)  # Math::DomainError: Numerical argument is out of domain - sqrt

# Cause 2: Negative logarithm
Math.log(-1)  # Math::DomainError: Numerical argument is out of domain - log

# Cause 3: Log of zero
Math.log(0)  # Math::DomainError: Numerical argument is out of domain - log

# Cause 4: Asin/Acos out of range
Math.asin(2)  # Math::DomainError: Numerical argument is out of domain - asin

# Cause 5: Acosh with value < 1
Math.acosh(0.5)  # Math::DomainError: Numerical argument is out of domain - acosh
```

## Solutions

### Fix 1: Validate input before calling math functions

```ruby
# Wrong
def safe_sqrt(value)
  Math.sqrt(value)
end

# Correct
def safe_sqrt(value)
  return nil if value < 0
  Math.sqrt(value)
end
```

### Fix 2: Use complex numbers for negative square roots

```ruby
# Wrong
Math.sqrt(-1)  # Math::DomainError

# Correct — use Complex numbers
require 'complex'
Math.sqrt(-1 + 0i)  # 0+1i
(-1).to_c.sqrt  # 0+1i
```

### Fix 3: Handle domain errors with rescue

```ruby
# Wrong
result = Math.log(input)

# Correct
begin
  result = Math.log(input)
rescue Math::DomainError
  puts "Cannot compute logarithm of #{input}"
  result = nil
end
```

### Fix 4: Use safe math helper methods

```ruby
module SafeMath
  def self.sqrt(value)
    return nil if value < 0
    Math.sqrt(value)
  end

  def self.log(value)
    return nil if value <= 0
    Math.log(value)
  end

  def self.asin(value)
    return nil if value < -1 || value > 1
    Math.asin(value)
  end
end

SafeMath.sqrt(-1)  # nil
SafeMath.log(-1)   # nil
```

## Related Errors

- [FloatDomainError](float-domain-error) — NaN or Infinity.
- [ZeroDivisionError](zero-division-error) — division by zero.
- [RangeError](range-error) — number too large for range.
