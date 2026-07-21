---
title: "[Solution] Deprecated Function Migration: Hash#select to Hash#filter"
description: "Migrate from deprecated Hash#select to Hash#filter."
deprecated_function: "hash.select { |k, v| }"
replacement_function: "hash.filter { |k, v| }"
languages: ["ruby"]
deprecated_since: "Ruby 2.7+"
---

# [Solution] Deprecated Function Migration: Hash#select to Hash#filter

The `hash.select { |k, v| }` has been deprecated in favor of `hash.filter { |k, v| }`.

## Migration Guide

filter is more descriptive

select works but filter is more descriptive.

## Before (Deprecated)

```ruby
result = hash.select { |k, v| v > 1 }
```

## After (Modern)

```ruby
result = hash.filter { |k, v| v > 1 }
```

## Key Differences

- filter is alias for select on Hash
- More descriptive name
