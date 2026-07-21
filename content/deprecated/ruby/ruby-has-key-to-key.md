---
title: "[Solution] Deprecated Function Migration: Hash.has_key? to Hash.key?"
description: "Migrate from deprecated Hash.has_key? to Hash.key? in Ruby for clarity."
deprecated_function: "hash.has_key?"
replacement_function: "hash.key?"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: Hash.has_key? to Hash.key?

The `hash.has_key?` has been deprecated in favor of `hash.key?`.

## Migration Guide

Hash.has_key? was renamed to Hash.key? for brevity. Both work, but key? is preferred.

## Before (Deprecated)

```ruby
hash = { name: "Alice", age: 30 }
if hash.has_key?(:name)
    puts "Name exists"
end
```

## After (Modern)

```ruby
hash = { name: "Alice", age: 30 }
if hash.key?(:name)
    puts "Name exists"
end
```

## Key Differences

- has_key? still works but key? is preferred
- has_value? was renamed to value?
- Both methods are aliases
