---
title: "[Solution] Deprecated Function Migration: force_encoding to encode"
description: "Migrate from deprecated force_encoding to encode."
deprecated_function: "str.force_encoding('UTF-8')"
replacement_function: "str.encode('UTF-8')"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: force_encoding to encode

The `str.force_encoding('UTF-8')` has been deprecated in favor of `str.encode('UTF-8')`.

## Migration Guide

encode performs actual conversion.

## Before (Deprecated)

```ruby
binary_str.force_encoding('UTF-8')
```

## After (Modern)

```ruby
utf8_str = binary_str.encode('UTF-8')
```

## Key Differences

- encode performs actual conversion
