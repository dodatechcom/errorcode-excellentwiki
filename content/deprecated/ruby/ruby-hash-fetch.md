---
title: "[Solution] Deprecated Function Migration: hash[key] to hash.fetch for mandatory keys"
description: "Migrate from deprecated hash[key] to hash.fetch for mandatory keys."
deprecated_function: "hash[key]"
replacement_function: "hash.fetch(key)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: hash[key] to hash.fetch for mandatory keys

The `hash[key]` has been deprecated in favor of `hash.fetch(key)`.

## Migration Guide

fetch raises KeyError for missing keys.

## Before (Deprecated)

```ruby
value = hash[key]
```

## After (Modern)

```ruby
value = hash.fetch(key)
```

## Key Differences

- fetch raises on missing keys
