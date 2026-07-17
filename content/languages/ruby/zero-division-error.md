---
title: "[Solution] Ruby ZeroDivisionError — Divided by 0 Fix"
description: "Fix Ruby ZeroDivisionError: divided by 0. Add input validation and handle edge cases in division operations."
languages: ["ruby"]
severities: ["error"]
error_types: ["division"]
weight: 120
---

# ZeroDivisionError — Divided by 0 Fix

A `ZeroDivisionError` is raised when you attempt to divide a number by zero. This applies to integer division, float division, and the modulo operator.

## Description

In Ruby, dividing by zero is always an error. Integer division by zero raises `ZeroDivisionError`. Float division by zero raises `FloatDomainError` if the result is `Infinity`, but `0/0` raises `ZeroDivisionError`.

Common scenarios:

- **Direct division by zero** — `10 / 0`.
- **Variable becomes zero at runtime** — divisor computed from data.
- **Modulo by zero** — `10 % 0`.
- **Integer zero** — `10 / 0` raises `ZeroDivisionError`.

## Common Causes

```ruby
# Cause 1: Direct division by zero
result = 10 / 0  # ZeroDivisionError: divided by 0

# Cause 2: Divisor computed from data
numbers = [10, 20, 0, 30]
for n in numbers
  result = 100 / n  # ZeroDivisionError when n == 0
end

# Cause 3: Modulo by zero
remainder = 10 % 0  # ZeroDivisionError: divided by 0

# Cause 4: Denominator from user input
print "Enter a number: "
denominator = gets.chomp.to_i
result = 100 / denominator  # Crashes if user enters 0
```

## Solutions

### Fix 1: Check divisor before dividing

```ruby
# Wrong
def divide(a, b)
  a / b
end

# Correct
def divide(a, b)
  return nil if b == 0
  a / b
end
```

### Fix 2: Use begin/rescue to handle zero gracefully

```ruby
# Wrong
result = numerator / denominator

# Correct
begin
  result = numerator / denominator
rescue ZeroDivisionError
  puts "Cannot divide by zero"
  result = nil
end
```

### Fix 3: Guard against zero in loops with data

```ruby
# Wrong
numbers = [10, 20, 0, 30]
numbers.each do |n|
  result = 100 / n
end

# Correct
numbers = [10, 20, 0, 30]
numbers.each do |n|
  if n != 0
    result = 100 / n
  else
    puts "Skipping zero, cannot divide 100 by #{n}"
  end
end
```

### Fix 4: Use Float division for division that may produce Infinity

```ruby
# Integer division raises ZeroDivisionError
10 / 0  # ZeroDivisionError

# Float division returns Infinity (no error)
10.0 / 0.0  # Infinity

# Use Float if you want Infinity instead of an error
result = numerator.to_f / denominator
```

## Related Errors

- [FloatDomainError](float-domain-error) — NaN or Infinity in domain operations.
- [Math::DomainError](math-domain-error) — math function domain error.
- [RangeError](range-error) — number too large for range.
