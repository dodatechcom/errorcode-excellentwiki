---
title: "[Solution] Ruby TypeError — No Implicit Conversion Fix"
description: "Fix Ruby TypeError: no implicit conversion. Learn why Ruby raises this error when mixing incompatible types and how to convert properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["typeerror", "type-conversion", "implicit-conversion", "ruby"]
weight: 5
---

# TypeError — No Implicit Conversion

A `TypeError` is raised when an operation receives an argument of the wrong type and Ruby can't implicitly convert it.

## Description

Ruby is dynamically typed but still enforces type compatibility for operations. When you mix incompatible types (like adding a String to an Integer), Ruby raises a `TypeError`.

Common causes:

- **Mixing incompatible types** — arithmetic between String and Integer
- **Wrong argument type** — passing a String where an Integer is expected
- **Frozen object modification** — trying to modify a frozen object
- **Encoding mismatches** — incompatible string encodings

## Common Causes

```ruby
# Cause 1: Adding String to Integer
"hello" + 123  # TypeError: no implicit conversion of Integer into String

# Cause 2: Wrong argument type
def multiply(a, b)
  a * b
end
multiply("hello", "world")  # TypeError: no implicit conversion of String into Integer

# Cause 3: Comparing incompatible types
"hello" > 123  # TypeError: comparison of String with Integer failed

# Cause 4: Frozen object modification
str = "hello".freeze
str << "world"  # TypeError: can't modify frozen String
```

## How to Fix

### Fix 1: Convert types explicitly

```ruby
# Wrong
"hello" + 123  # TypeError

# Correct
"hello" + 123.to_s  # "hello123"
```

### Fix 2: Validate argument types

```ruby
# Wrong
def multiply(a, b)
  a * b
end

# Correct
def multiply(a, b)
  raise ArgumentError, "Arguments must be numbers" unless a.is_a?(Numeric) && b.is_a?(Numeric)
  a * b
end
```

### Fix 3: Use explicit conversions

```ruby
# Wrong
Integer("abc")  # ArgumentError, but similar concept

# Correct
"123".to_i  # 123
"3.14".to_f  # 3.14
123.to_s  # "123"
```

### Fix 4: Handle frozen strings

```ruby
# Wrong
str = "hello".freeze
str << "world"  # TypeError

# Correct
str = +("hello")  # Creates mutable copy
str << "world"  # "helloworld"
```

## Examples

```ruby
# Example 1: Common type mismatch
a = "10"
b = 20
# a + b  # TypeError
a.to_i + b  # 30

# Example 2: Array operations
mixed = [1, "two", 3]
mixed.sum  # TypeError: no implicit conversion of String into Integer
mixed.select { |x| x.is_a?(Integer) }.sum  # 4
```

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method for object
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}}) — wrong number or type of arguments
- [FrozenError]({{< relref "/languages/ruby/frozen-error" >}}) — modifying frozen object
