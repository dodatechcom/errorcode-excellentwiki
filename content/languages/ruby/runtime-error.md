---
title: "[Solution] Ruby RuntimeError — Generic Runtime Error Fix"
description: "Fix Ruby RuntimeError. Understand when raise is called with a generic message and how to handle unexpected runtime conditions."
languages: ["ruby"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["runtimeerror", "raise", "runtime", "exception"]
weight: 20
---

# RuntimeError — Generic Runtime Error Fix

A `RuntimeError` is the default exception raised by `raise` without specifying an exception class. It signals an unexpected condition during program execution.

## Description

`RuntimeError` is the catch-all error in Ruby when you call `raise` with a message but no specific exception class. It's often used for application-level errors that don't fit standard exception categories.

Common scenarios:

- **Explicit `raise "message"`** — most common source.
- **Guard clauses** — raising on invalid state.
- **Unreachable code paths** — signaling unexpected conditions.
- **Frozen string modification** — `RuntimeError: can't modify frozen String`.

## Common Causes

```ruby
# Cause 1: Explicit raise with generic message
def process(order)
  raise "Order cannot be nil" if order.nil?
  raise "Order already processed" if order.processed?
end

# Cause 2: Frozen string modification (common in Ruby 3+)
str = "hello".freeze
str << " world"  # RuntimeError: can't modify frozen String

# Cause 3: Raise in a method without a specific exception
def calculate_tax(income)
  raise "Income must be positive" if income <= 0
  income * 0.3
end

# Cause 4: Raise in a block or iterator
[1, 2, 3].each do |n|
  raise "Unexpected negative number" if n < 0
end
```

## Solutions

### Fix 1: Use specific exception classes

```ruby
# Wrong
def process(order)
  raise "Order is invalid" unless order.valid?
end

# Correct
class OrderError < StandardError; end
class InvalidOrderError < OrderError; end

def process(order)
  raise InvalidOrderError, "Order is invalid" unless order.valid?
end
```

### Fix 2: Handle frozen string errors

```ruby
# Wrong
str = "hello".freeze
str << " world"  # RuntimeError

# Correct — use + to unfreeze or gsub to create new string
str = "hello".freeze
new_str = str + " world"       # Creates a new string
new_str = str.gsub("hello", "hi")  # Returns a new string

# Or use String.new to create a mutable string
str = String.new("hello")
str << " world"  # Works fine
```

### Fix 3: Rescue specific exceptions

```ruby
# Wrong — rescuing all RuntimeErrors
begin
  risky_operation
rescue RuntimeError => e
  puts e.message
end

# Correct — rescue the specific error you expect
begin
  risky_operation
rescue InvalidOrderError => e
  puts "Invalid order: #{e.message}"
rescue StandardError => e
  puts "Unexpected error: #{e.message}"
end
```

### Fix 4: Validate inputs early with guard clauses

```ruby
# Wrong — validation buried in logic
def transfer(from_account, to_account, amount)
  # ... lots of code ...
  raise "Invalid amount" if amount <= 0
end

# Correct — validate at the top
def transfer(from_account, to_account, amount)
  raise ArgumentError, "Amount must be positive" if amount <= 0
  raise ArgumentError, "Accounts must be different" if from_account == to_account

  # ... main logic ...
end
```

## Related Errors

- [ArgumentError](argument-error) — wrong number of arguments passed to a method.
- [TypeError](type-error) — wrong argument type passed to a method.
- [FrozenError](frozen-error) — can't modify a frozen object.
