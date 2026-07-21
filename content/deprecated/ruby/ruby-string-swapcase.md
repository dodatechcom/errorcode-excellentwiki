---
title: "[Solution] Deprecated Function Migration: String#swapcase! to non-mutating methods"
description: "Migrate from deprecated String#swapcase! to non-mutating string methods."
deprecated_function: "str.swapcase!"
replacement_function: "str.swapcase"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: String#swapcase! to non-mutating methods

The `str.swapcase!` has been deprecated in favor of `str.swapcase`.

## Migration Guide

Non-mutating methods are safer and more predictable

Mutating methods (!) can cause unexpected side effects. Non-mutating methods return new strings.

## Before (Deprecated)

```ruby
str = "Hello World"
str.downcase!
str.strip!
str.gsub!(/old/, "new")
```

## After (Modern)

```ruby
str = "Hello World"
new_str = str.downcase
new_str = str.strip
new_str = str.gsub(/old/, "new")

# Or chain
new_str = str.downcase.strip.gsub(/old/, "new")
```

## Key Differences

- Non-mutating methods return new strings
- Safer -- no unexpected side effects
- Method chaining with non-mutating methods
- Use ! only when mutation is intended
