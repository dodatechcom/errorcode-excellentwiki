---
title: "[Solution] Deprecated Function Migration: Hash#to_proc to dig"
description: "Migrate from deprecated Hash#to_proc to dig for nested access."
deprecated_function: "hash.to_proc.call(key)"
replacement_function: "hash.dig(key1, key2)"
languages: ["ruby"]
deprecated_since: "Ruby 2.3+"
---

# [Solution] Deprecated Function Migration: Hash#to_proc to dig

The `hash.to_proc.call(key)` has been deprecated in favor of `hash.dig(key1, key2)`.

## Migration Guide

dig handles nil safely.

## Before (Deprecated)

```ruby
value = hash[:a][:b]  # NoMethodError if :a is nil
```

## After (Modern)

```ruby
value = hash.dig(:a, :b)  # returns nil if any key is missing
```

## Key Differences

- dig handles nil safely
