---
title: "[Solution] Ruby TypeError — No Implicit Conversion Fix"
description: "Fix Ruby TypeError: no implicit conversion. Ensure correct types are passed to methods and handle type coercion properly."
languages: ["ruby"]
severities: ["error"]
error_types: ["type"]
weight: 30
---

# TypeError — No Implicit Conversion Fix

A `TypeError` is raised when an object is of the wrong type for an operation. The most common form is "no implicit conversion of X into Y."

## Description

Ruby is dynamically typed but still enforces type expectations in many operations. A `TypeError` occurs when you try to use an object where a different type is required.

Common scenarios:

- **String vs Integer** — passing a string where an integer is expected, or vice versa.
- **Wrong receiver** — calling a method on an object that doesn't support it.
- **Type coercion failure** — implicit conversion methods (`to_i`, `to_s`) not available.
- **Frozen object mutation** — attempting to modify a frozen object (also `FrozenError`).

## Common Causes

```ruby
# Cause 1: String where Integer expected
"hello" + 42  # TypeError: no implicit conversion of Integer into String

# Cause 2: Integer where String expected
"Score: " + 100  # TypeError: no implicit conversion of Integer into String

# Cause 3: Nil where String expected
name = nil
puts "Hello, " + name  # TypeError: no implicit conversion of nil into String

# Cause 4: Wrong type for array/hash operations
arr = [1, 2, 3]
arr.slice("0", 2)  # TypeError: no implicit conversion of String into Integer
```

## Solutions

### Fix 1: Convert types explicitly

```ruby
# Wrong
age = "25"
next_age = age + 1  # TypeError

# Correct
age = "25"
next_age = age.to_i + 1  # 26

# Or use Integer() for strict conversion
next_age = Integer(age) + 1
```

### Fix 2: Use string interpolation for mixed types

```ruby
# Wrong
score = 100
message = "Score: " + score  # TypeError

# Correct
message = "Score: #{score}"  # "Score: 100"
```

### Fix 3: Handle nil safely

```ruby
# Wrong
name = nil
puts "Hello, " + name  # TypeError

# Correct
name = nil
puts "Hello, #{name || 'World'}"  # "Hello, World"

# Or use to_s which returns "" for nil
puts "Hello, " + name.to_s  # "Hello, "
```

### Fix 4: Use safe navigation operator

```ruby
# Wrong
user = nil
user.name  # NoMethodError (related)

# Correct — safe navigation
user&.name  # nil
```

## Related Errors

- [NoMethodError](no-method-error) — method doesn't exist on the object.
- [ArgumentError](argument-error) — wrong number of arguments passed to a method.
- [FrozenError](frozen-error) — can't modify a frozen object.
