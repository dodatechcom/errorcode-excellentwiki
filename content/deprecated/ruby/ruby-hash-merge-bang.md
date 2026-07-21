---
title: "[Solution] Deprecated Function Migration: merge! to merge for non-destructive merge"
description: "Migrate from deprecated merge! to merge for creating new hashes."
deprecated_function: "hash.merge!(other)"
replacement_function: "hash.merge(other)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: merge! to merge for non-destructive merge

The `hash.merge!(other)` has been deprecated in favor of `hash.merge(other)`.

## Migration Guide

merge returns new hash.

## Before (Deprecated)

```ruby
hash1.merge!(hash2)
```

## After (Modern)

```ruby
merged = hash1.merge(hash2)
```

## Key Differences

- merge returns new hash
