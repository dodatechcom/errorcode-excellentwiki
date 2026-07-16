---
title: "[Solution] Ruby ZeroDivisionError — Divided by 0 Fix"
description: "Fix Ruby ZeroDivisionError: divided by 0. Learn how to prevent division by zero and handle edge cases in arithmetic operations."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["zerodivisionerror", "division-by-zero", "arithmetic", "ruby"]
weight: 5
---

# ZeroDivisionError — Divided by 0

A `ZeroDivisionError` is raised when you attempt to divide a number by zero.

## Description

Mathematical division by zero is undefined. Ruby raises `ZeroDivisionError` whenever you attempt to divide an integer or float by zero. This can happen in calculations, averages, percentages, and ratios.

Common causes:

- **User input as divisor** — dividing by unvalidated user input
- **Empty collection averages** — dividing by count of empty array
- **Percentage calculations** — dividing by total that's zero
- **Config values** — config parameters defaulting to zero

## Common Causes

```ruby
# Cause 1: Direct division by zero
10 / 0  # ZeroDivisionError: divided by 0

# Cause 2: User input as divisor
total = 100
count = user_input.to_i
average = total / count  # ZeroDivisionError if count is 0

# Cause 3: Empty array average
scores = []
average = scores.sum / scores.length  # ZeroDivisionError: divided by 0

# Cause 4: Float division by zero
10.0 / 0.0  # Infinity (no error for Float, but unexpected result)
```

## How to Fix

### Fix 1: Check divisor before division

```ruby
# Wrong
result = a / b  # ZeroDivisionError

# Correct
result = b != 0 ? a / b : nil
```

### Fix 2: Use guard clause

```ruby
# Wrong
def average(numbers)
  numbers.sum / numbers.length
end

# Correct
def average(numbers)
  return nil if numbers.empty?
  numbers.sum.to_f / numbers.length
end
```

### Fix 3: Use Float division

```ruby
# Wrong
average = total / count  # Integer division, possible ZeroDivisionError

# Correct
average = total.to_f / count
```

### Fix 4: Use safe division method

```ruby
# Wrong
result = a / b  # ZeroDivisionError

# Correct
def safe_divide(a, b)
  b.zero? ? 0 : a / b
end
```

## Examples

```ruby
# Example 1: Safe average calculation
def calculate_average(values)
  return 0.0 if values.empty?
  values.sum.to_f / values.length
end
calculate_average([10, 20, 30])  # 20.0
calculate_average([])  # 0.0

# Example 2: Percentage calculation
def percentage(part, total)
  return 0.0 if total.zero?
  (part.to_f / total * 100).round(2)
end
percentage(25, 100)  # 25.0
percentage(25, 0)  # 0.0
```

## Related Errors

- [FloatDomainError]({{< relref "/languages/ruby/float-domain-error" >}}) — invalid float operation
- [Math::DomainError]({{< relref "/languages/ruby/math-domain-error" >}}) — math function domain error
- [ArgumentError]({{< relref "/languages/ruby/argumenterror-ruby" >}}) — wrong number of arguments
