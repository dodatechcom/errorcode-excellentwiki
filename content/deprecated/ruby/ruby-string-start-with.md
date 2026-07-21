---
title: "[Solution] Deprecated Function Migration: str[0..n] to str.start_with?"
description: "Migrate from deprecated string slicing to start_with?."
deprecated_function: "str[0..n] == prefix"
replacement_function: "str.start_with?(prefix)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: str[0..n] to str.start_with?

The `str[0..n] == prefix` has been deprecated in favor of `str.start_with?(prefix)`.

## Migration Guide

start_with? is more readable.

## Before (Deprecated)

```ruby
if str[0..4] == 'Hello' { }
```

## After (Modern)

```ruby
if str.start_with?('Hello') { }
```

## Key Differences

- start_with? is more readable
