---
title: "[Solution] Deprecated Function Migration: String concatenation to interpolation"
description: "Migrate from deprecated string concatenation patterns to string interpolation in Ruby."
deprecated_function: "str1 +   + str2"
replacement_function: "#{str1} #{str2}"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: String concatenation to interpolation

The `str1 + " " + str2` has been deprecated in favor of `"#{str1} #{str2}"`.

## Migration Guide

String interpolation is faster and more readable than concatenation with +.

## Before (Deprecated)

```ruby
name = "Alice"
greeting = "Hello, " + name + "!"
log = "User: " + name + " at " + time
```

## After (Modern)

```ruby
name = "Alice"
greeting = "Hello, #{name}!"
log = "User: #{name} at #{time}"

# Shovel operator for mutation
str = "Hello"
str << ", World!"
```

## Key Differences

- Interpolation is faster than concatenation
- << mutates the string (no new object)
- + creates a new string each time
- Use interpolation for readability
