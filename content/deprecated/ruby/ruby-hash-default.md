---
title: "[Solution] Deprecated Function Migration: Hash[] constructor to literal syntax"
description: "Migrate from deprecated Hash[] constructor to hash literal syntax in Ruby."
deprecated_function: "Hash[key, value]"
replacement_function: "{ key: value }"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: Hash[] constructor to literal syntax

The `Hash[key, value]` has been deprecated in favor of `{ key: value }`.

## Migration Guide

Hash literal is more concise and readable

Hash[] constructor is verbose. Hash literal syntax is preferred.

## Before (Deprecated)

```ruby
hash = Hash[:name, "Alice", :age, 30]
hash = Hash.new("default")
```

## After (Modern)

```ruby
hash = { name: "Alice", age: 30 }

# With default value
hash = Hash.new { |h, k| h[k] = [] }

# Shorthand syntax (Ruby 3.1+)
name = "Alice"
age = 30
hash = { name:, age: }
```

## Key Differences

- Hash literal is more concise
- Shorthand syntax in Ruby 3.1+
- Hash[] for dynamic construction
- Hash.new for default values
