---
title: "[Solution] Deprecated Function Migration: str.length to str.bytesize for byte count"
description: "Migrate from deprecated str.length to str.bytesize for byte count."
deprecated_function: "str.length"
replacement_function: "str.bytesize"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: str.length to str.bytesize for byte count

The `str.length` has been deprecated in favor of `str.bytesize`.

## Migration Guide

bytesize gives actual byte count.

## Before (Deprecated)

```ruby
len = str.length  # character count
```

## After (Modern)

```ruby
len = str.bytesize  # byte count
```

## Key Differences

- bytesize gives actual byte count
