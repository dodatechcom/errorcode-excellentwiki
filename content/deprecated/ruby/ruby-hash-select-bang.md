---
title: "[Solution] Deprecated Function Migration: Hash#select! to Hash#select"
description: "Migrate from deprecated Hash#select! to Hash#select."
deprecated_function: "hash.select! { |k, v| v > 0 }"
replacement_function: "hash.select { |k, v| v > 0 }"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: Hash#select! to Hash#select

The `hash.select! { |k, v| v > 0 }` has been deprecated in favor of `hash.select { |k, v| v > 0 }`.

## Migration Guide

select returns new hash.

## Before (Deprecated)

```ruby
hash.select! { |k, v| v > 0 }
```

## After (Modern)

```ruby
filtered = hash.select { |k, v| v > 0 }
```

## Key Differences

- select returns new hash
