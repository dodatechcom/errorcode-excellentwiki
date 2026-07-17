---
title: "[Solution] Ruby TypeError — Type Mismatch Fix"
description: "Fix Ruby TypeError: type mismatch. Learn why incompatible types cause this error and how to convert or validate types."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["typeerror", "type-mismatch", "incompatible", "ruby"]
weight: 5
---

## What This Error Means

A `TypeError` is raised when an operation is performed on an object of an incompatible type. Ruby is dynamically typed but still enforces type constraints for certain operations.

## Common Causes

- Converting incompatible types (e.g., `nil` to Integer)
- Passing wrong type to a method expecting a specific type
- Comparing incompatible types
- Attempting to freeze an incompatible object

## How to Fix

```ruby
# WRONG: Incompatible type conversion
nil + 1  # TypeError: no implicit conversion of nil into Integer

# CORRECT: Validate and convert
value = nil
result = value.to_i if value  # 0
```

```ruby
# WRONG: Wrong type for array operations
"hello"[0]  # Works, but:
123[0]  # TypeError: no implicit conversion of Integer into String

# CORRECT: Ensure correct type
num = 123
str = num.to_s
str[0]  # "1"
```

```ruby
# WRONG: Comparing incompatible types
"hello" > 123  # TypeError: no implicit conversion of Integer into String

# CORRECT: Compare same types
"hello".length > 123  # false (comparing integers)
```

```ruby
# WRONG: Trying to freeze wrong type
123.freeze  # Works, but some objects have restrictions

# CORRECT: Check object type before freezing
obj.freeze if obj.respond_to?(:freeze)
```

## Examples

```ruby
# Example 1: Nil in arithmetic
x = nil
y = x + 5  # TypeError

# Example 2: Wrong method argument type
[1, 2, 3].join(",")  # "1,2,3"
[1, 2, 3].join(123)  # TypeError: no implicit conversion of Integer into String

# Example 3: Encoding mismatch
"hello".encode("UTF-8")  # OK
```

## Related Errors

- [NoMethodError](nomethoderror-ruby) — undefined method on object
- [ArgumentError](argumenterror-ruby) — wrong number of arguments
- [NameError](nameerror-ruby) — uninitialized constant
